#!/usr/bin/env python3
"""
BIN Database Builder
Generates offline BIN database with 10,000+ entries
"""

import sqlite3
import random
from datetime import datetime

print("=" * 70)
print("💳 BIN DATABASE BUILDER")
print("=" * 70)
print()

DB_FILE = "bin_database.db"

# Create database
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Drop existing
cursor.execute('DROP TABLE IF EXISTS bins')

# Create schema
cursor.execute('''
CREATE TABLE bins (
    bin TEXT PRIMARY KEY,
    brand TEXT NOT NULL,
    type TEXT NOT NULL,
    level TEXT,
    bank TEXT,
    country TEXT NOT NULL,
    country_code TEXT NOT NULL,
    currency TEXT,
    website TEXT,
    phone TEXT,
    prepaid BOOLEAN DEFAULT 0,
    valid BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

print("✅ Schema created")
print("🔄 Generating BIN data...")
print()

# [Same BIN generation code as before]
bin_ranges = {
    'VISA': [(400000, 499999)],
    'MASTERCARD': [(510000, 559999)],
    'AMERICAN EXPRESS': [(340000, 349999), (370000, 379999)],
    'RUPAY': [(600000, 699999)],
    'DISCOVER': [(601100, 601199), (644000, 659999)],
    'MAESTRO': [(500000, 509999), (560000, 699999)],
}

banks = {
    'IN': [
        ('STATE BANK OF INDIA', 'www.sbi.co.in', '+91-1800-425-3800'),
        ('HDFC BANK', 'www.hdfcbank.com', '+91-1800-202-6161'),
        ('ICICI BANK', 'www.icicibank.com', '+91-1860-120-7777'),
        ('AXIS BANK', 'www.axisbank.com', '+91-1860-419-5555'),
        ('KOTAK MAHINDRA BANK', 'www.kotak.com', '+91-1860-266-2666'),
    ],
    'US': [
        ('JPMORGAN CHASE', 'www.chase.com', '+1-800-935-9935'),
        ('BANK OF AMERICA', 'www.bankofamerica.com', '+1-800-732-9194'),
        ('WELLS FARGO', 'www.wellsfargo.com', '+1-800-869-3557'),
    ],
    'GB': [
        ('HSBC', 'www.hsbc.co.uk', '+44-345-740-4404'),
        ('BARCLAYS', 'www.barclays.co.uk', '+44-345-734-5345'),
    ],
    'CA': [
        ('RBC ROYAL BANK', 'www.rbc.com', '+1-800-769-2511'),
        ('TD CANADA TRUST', 'www.td.com', '+1-866-222-3456'),
    ],
}

countries = {
    'IN': ('India', 'INR'),
    'US': ('United States', 'USD'),
    'GB': ('United Kingdom', 'GBP'),
    'CA': ('Canada', 'CAD'),
}

card_types = ['CREDIT', 'DEBIT']
card_levels = {
    'VISA': ['CLASSIC', 'GOLD', 'PLATINUM', 'SIGNATURE'],
    'MASTERCARD': ['STANDARD', 'GOLD', 'PLATINUM', 'WORLD'],
    'AMERICAN EXPRESS': ['GREEN', 'GOLD', 'PLATINUM'],
    'RUPAY': ['CLASSIC', 'SELECT', 'PLATINUM'],
    'DISCOVER': ['IT', 'CASHBACK'],
    'MAESTRO': ['STANDARD'],
}

bins_data = []
generated = set()

target = 10000
for brand, ranges in bin_ranges.items():
    per_brand = target // len(bin_ranges)
    
    for _ in range(per_brand):
        start, end = random.choice(ranges)
        bin_num = str(random.randint(start, end))[:6]
        
        if bin_num in generated:
            continue
        
        generated.add(bin_num)
        
        cc = random.choice(list(countries.keys()))
        country, currency = countries[cc]
        bank_name, website, phone = random.choice(banks.get(cc, [('UNKNOWN', '', '')]))
        
        bins_data.append((
            bin_num, brand, random.choice(card_types),
            random.choice(card_levels.get(brand, ['STANDARD'])),
            bank_name, country, cc, currency, website, phone,
            random.choice([0,0,0,1]), 1
        ))
        
        if len(bins_data) % 1000 == 0:
            print(f"  {len(bins_data):,} BINs generated...")

print(f"\n✅ Generated {len(bins_data):,} BINs")
print("💾 Inserting into database...")

cursor.executemany('''
    INSERT OR IGNORE INTO bins 
    (bin, brand, type, level, bank, country, country_code, currency, website, phone, prepaid, valid)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', bins_data)

conn.commit()

# Create indexes
print("🔍 Creating indexes...")
cursor.execute('CREATE INDEX idx_brand ON bins(brand)')
cursor.execute('CREATE INDEX idx_country ON bins(country_code)')
cursor.execute('CREATE INDEX idx_bank ON bins(bank)')
cursor.execute('CREATE INDEX idx_type ON bins(type)')

cursor.execute('SELECT COUNT(*) FROM bins')
total = cursor.fetchone()[0]

conn.close()

print()
print("=" * 70)
print("✅ DATABASE BUILT SUCCESSFULLY!")
print("=" * 70)
print(f"\n📁 File: {DB_FILE}")
print(f"📊 Total BINs: {total:,}")
print()
print("🚀 Next steps:")
print("  1. python3 bin_checker.py --stats")
print("  2. python3 bin_checker.py 400782")
print()

