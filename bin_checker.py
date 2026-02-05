#!/usr/bin/env python3
"""
Advanced BIN Checker - Offline Database
No API required - 9000+ BINs

Usage:
    python3 bin_checker.py 400782
    python3 bin_checker.py --search visa
    python3 bin_checker.py --country IN
    python3 bin_checker.py --bank "HDFC"
"""

import sqlite3
import sys
import json
from datetime import datetime

DB_FILE = 'bin_database.db'

class BINChecker:
    def __init__(self):
        self.conn = sqlite3.connect(DB_FILE)
        self.cursor = self.conn.cursor()
    
    def lookup(self, bin_number):
        """Lookup specific BIN"""
        bin_number = str(bin_number).strip()[:6]
        
        self.cursor.execute('SELECT * FROM bins WHERE bin = ?', (bin_number,))
        result = self.cursor.fetchone()
        
        if result:
            return self._format_result(result)
        return None
    
    def search_by_brand(self, brand):
        """Search BINs by brand"""
        self.cursor.execute(
            'SELECT * FROM bins WHERE UPPER(brand) LIKE ? LIMIT 50',
            (f'%{brand.upper()}%',)
        )
        return [self._format_result(r) for r in self.cursor.fetchall()]
    
    def search_by_country(self, country_code):
        """Search BINs by country"""
        self.cursor.execute(
            'SELECT * FROM bins WHERE country_code = ? LIMIT 50',
            (country_code.upper(),)
        )
        return [self._format_result(r) for r in self.cursor.fetchall()]
    
    def search_by_bank(self, bank_name):
        """Search BINs by bank name"""
        self.cursor.execute(
            'SELECT * FROM bins WHERE UPPER(bank) LIKE ? LIMIT 50',
            (f'%{bank_name.upper()}%',)
        )
        return [self._format_result(r) for r in self.cursor.fetchall()]
    
    def get_stats(self):
        """Get database statistics"""
        stats = {}
        
        # Total
        self.cursor.execute('SELECT COUNT(*) FROM bins')
        stats['total'] = self.cursor.fetchone()[0]
        
        # By country
        self.cursor.execute('''
            SELECT country_code, country, COUNT(*) 
            FROM bins 
            GROUP BY country_code 
            ORDER BY COUNT(*) DESC
        ''')
        stats['countries'] = [
            {'code': r[0], 'name': r[1], 'count': r[2]} 
            for r in self.cursor.fetchall()
        ]
        
        # By brand
        self.cursor.execute('''
            SELECT brand, COUNT(*) 
            FROM bins 
            GROUP BY brand 
            ORDER BY COUNT(*) DESC
        ''')
        stats['brands'] = [
            {'brand': r[0], 'count': r[1]} 
            for r in self.cursor.fetchall()
        ]
        
        # By type
        self.cursor.execute('''
            SELECT type, COUNT(*) 
            FROM bins 
            GROUP BY type
        ''')
        stats['types'] = [
            {'type': r[0], 'count': r[1]} 
            for r in self.cursor.fetchall()
        ]
        
        return stats
    
    def _format_result(self, row):
        """Format database row as dict"""
        return {
            'bin': row[0],
            'brand': row[1],
            'type': row[2],
            'level': row[3],
            'bank': row[4],
            'country': row[5],
            'country_code': row[6],
            'currency': row[7],
            'website': row[8],
            'phone': row[9],
            'prepaid': bool(row[10]),
            'valid': bool(row[11])
        }
    
    def close(self):
        self.conn.close()

def print_bin_info(data):
    """Pretty print BIN information"""
    print("=" * 70)
    print(f"💳 BIN: {data['bin']}")
    print("=" * 70)
    print(f"Brand:        {data['brand']}")
    print(f"Type:         {data['type']}")
    print(f"Level:        {data['level'] or 'N/A'}")
    print(f"Bank:         {data['bank']}")
    print(f"Country:      {data['country']} ({data['country_code']})")
    print(f"Currency:     {data['currency']}")
    print(f"Website:      {data['website'] or 'N/A'}")
    print(f"Phone:        {data['phone'] or 'N/A'}")
    print(f"Prepaid:      {'✅ Yes' if data['prepaid'] else '❌ No'}")
    print(f"Valid:        {'✅ Yes' if data['valid'] else '❌ No'}")
    print("=" * 70)

def print_stats(stats):
    """Pretty print statistics"""
    print("=" * 70)
    print("📊 DATABASE STATISTICS")
    print("=" * 70)
    print(f"\nTotal BINs: {stats['total']:,}")
    
    print("\n🌍 By Country:")
    for c in stats['countries']:
        print(f"   {c['name']} ({c['code']}): {c['count']:,} BINs")
    
    print("\n💳 By Brand:")
    for b in stats['brands']:
        print(f"   {b['brand']}: {b['count']:,} BINs")
    
    print("\n📇 By Type:")
    for t in stats['types']:
        print(f"   {t['type']}: {t['count']:,} BINs")
    
    print("=" * 70)

def main():
    if len(sys.argv) < 2:
        print("💳 BIN Checker - Advanced Offline Tool")
        print("=" * 70)
        print("\nUsage:")
        print("  Lookup BIN:       python3 bin_checker.py 400782")
        print("  Search brand:     python3 bin_checker.py --brand visa")
        print("  Search country:   python3 bin_checker.py --country IN")
        print("  Search bank:      python3 bin_checker.py --bank HDFC")
        print("  Get statistics:   python3 bin_checker.py --stats")
        print("  JSON output:      python3 bin_checker.py 400782 --json")
        print("\nExamples:")
        print("  python3 bin_checker.py 512648")
        print("  python3 bin_checker.py --brand mastercard")
        print("  python3 bin_checker.py --country US")
        print("  python3 bin_checker.py --bank 'STATE BANK'")
        sys.exit(0)
    
    checker = BINChecker()
    json_output = '--json' in sys.argv
    
    try:
        if '--stats' in sys.argv:
            stats = checker.get_stats()
            if json_output:
                print(json.dumps(stats, indent=2))
            else:
                print_stats(stats)
        
        elif '--brand' in sys.argv:
            idx = sys.argv.index('--brand')
            brand = sys.argv[idx + 1]
            results = checker.search_by_brand(brand)
            
            if json_output:
                print(json.dumps(results, indent=2))
            else:
                print(f"\n🔍 Found {len(results)} BINs for brand '{brand}':\n")
                for r in results[:10]:
                    print(f"  {r['bin']} - {r['brand']} {r['type']} - {r['bank']}")
                if len(results) > 10:
                    print(f"  ... and {len(results)-10} more")
        
        elif '--country' in sys.argv:
            idx = sys.argv.index('--country')
            country = sys.argv[idx + 1]
            results = checker.search_by_country(country)
            
            if json_output:
                print(json.dumps(results, indent=2))
            else:
                print(f"\n🔍 Found {len(results)} BINs for country '{country}':\n")
                for r in results[:10]:
                    print(f"  {r['bin']} - {r['brand']} {r['type']} - {r['bank']}")
                if len(results) > 10:
                    print(f"  ... and {len(results)-10} more")
        
        elif '--bank' in sys.argv:
            idx = sys.argv.index('--bank')
            bank = sys.argv[idx + 1]
            results = checker.search_by_bank(bank)
            
            if json_output:
                print(json.dumps(results, indent=2))
            else:
                print(f"\n🔍 Found {len(results)} BINs for bank '{bank}':\n")
                for r in results[:10]:
                    print(f"  {r['bin']} - {r['brand']} {r['type']} - {r['country']}")
                if len(results) > 10:
                    print(f"  ... and {len(results)-10} more")
        
        else:
            # Direct BIN lookup
            bin_num = sys.argv[1]
            result = checker.lookup(bin_num)
            
            if result:
                if json_output:
                    print(json.dumps(result, indent=2))
                else:
                    print_bin_info(result)
            else:
                print(f"❌ BIN {bin_num} not found in database")
                print(f"\n💡 Try: python3 bin_checker.py --stats")
    
    finally:
        checker.close()

if __name__ == "__main__":
    main()
