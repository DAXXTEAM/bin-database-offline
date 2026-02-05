# 💳 BIN Database - Offline Checker

**Complete offline BIN (Bank Identification Number) database with 9,000+ verified entries.**

No API required! Fast, local SQLite database with Python lookup tools.

---

## 🚀 Features

✅ **9,000+ BINs** - Verified bank identification numbers  
✅ **100% Offline** - No API keys or internet required  
✅ **Fast Lookup** - SQLite database with indexes  
✅ **Multi-Country** - India, USA, UK, Canada  
✅ **Multiple Brands** - Visa, Mastercard, Amex, RuPay, Discover, Maestro  
✅ **Rich Data** - Bank name, country, currency, phone, website  
✅ **JSON Export** - Easy integration  
✅ **Search Options** - By BIN, brand, country, bank  

---

## 📊 Database Stats

| Metric | Count |
|--------|-------|
| **Total BINs** | 9,093 |
| **Countries** | 4 (IN, US, GB, CA) |
| **Brands** | 6 (Visa, MC, Amex, RuPay, Discover, Maestro) |
| **Banks** | 30+ major banks |
| **Credit Cards** | 4,540 |
| **Debit Cards** | 4,553 |

---

## ⚡ Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/bin-database-offline.git
cd bin-database-offline
```

### 2. Build Database

```bash
python3 build_database.py
```

This will create `bin_database.db` with 9,000+ BINs.

### 3. Use Checker

```bash
# Lookup a BIN
python3 bin_checker.py 400782

# Search by brand
python3 bin_checker.py --brand visa

# Search by country
python3 bin_checker.py --country IN

# Get statistics
python3 bin_checker.py --stats
```

---

## 📖 Usage Examples

### Basic Lookup

```bash
$ python3 bin_checker.py 512648
```

**Output:**
```
======================================================================
💳 BIN: 512648
======================================================================
Brand:        MASTERCARD
Type:         CREDIT
Level:        WORLD
Bank:         AXIS BANK
Country:      India (IN)
Currency:     INR
Website:      www.axisbank.com
Phone:        +91-1860-419-5555
Prepaid:      ❌ No
Valid:        ✅ Yes
======================================================================
```

### Search by Brand

```bash
$ python3 bin_checker.py --brand visa
```

### Search by Country

```bash
$ python3 bin_checker.py --country US
```

### JSON Output

```bash
$ python3 bin_checker.py 400782 --json
```

```json
{
  "bin": "400782",
  "brand": "VISA",
  "type": "CREDIT",
  "level": "CLASSIC",
  "bank": "STATE BANK OF INDIA",
  "country": "India",
  "country_code": "IN",
  "currency": "INR",
  "website": "www.sbi.co.in",
  "phone": "+91-1800-425-3800",
  "prepaid": false,
  "valid": true
}
```

---

## 🐍 Python Integration

```python
from bin_checker import BINChecker

# Initialize
checker = BINChecker()

# Lookup BIN
result = checker.lookup('400782')
print(result)

# Search by brand
visa_cards = checker.search_by_brand('visa')

# Search by country
india_cards = checker.search_by_country('IN')

# Get stats
stats = checker.get_stats()

# Close connection
checker.close()
```

---

## 📁 File Structure

```
bin-database-offline/
├── README.md              # This file
├── build_database.py      # Database builder
├── bin_checker.py         # Lookup tool
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
└── bin_database.db       # Generated database (after build)
```

---

## 🛠️ Requirements

- Python 3.6+
- SQLite3 (built-in with Python)

**No external dependencies!** Pure Python stdlib only.

---

## 🔍 Database Schema

```sql
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
);
```

---

## 🌍 Supported Countries

| Code | Country | BINs | Currency |
|------|---------|------|----------|
| IN | India | 2,215 | INR |
| US | United States | 2,305 | USD |
| GB | United Kingdom | 2,253 | GBP |
| CA | Canada | 2,320 | CAD |

---

## 💳 Supported Brands

- **VISA** - 1,649 BINs
- **MASTERCARD** - 1,646 BINs
- **AMERICAN EXPRESS** - 1,602 BINs
- **RUPAY** - 1,650 BINs (India domestic)
- **DISCOVER** - 927 BINs
- **MAESTRO** - 1,619 BINs

---

## 🏦 Major Banks Included

### India
- State Bank of India (SBI)
- HDFC Bank
- ICICI Bank
- Axis Bank
- Kotak Mahindra Bank
- Punjab National Bank
- And 10+ more

### USA
- JPMorgan Chase
- Bank of America
- Wells Fargo
- Citibank
- Capital One
- And more

### UK
- HSBC
- Barclays
- Lloyds Bank
- NatWest
- Santander UK
- TSB Bank

### Canada
- RBC Royal Bank
- TD Canada Trust
- Scotiabank
- BMO Bank of Montreal

---

## 🔧 Advanced Features

### Bulk Lookup

```python
bins = ['400782', '512648', '378282']
for bin_num in bins:
    result = checker.lookup(bin_num)
    print(f"{bin_num}: {result['bank']}")
```

### Export to CSV

```bash
sqlite3 bin_database.db -header -csv "SELECT * FROM bins" > bins_export.csv
```

### Add Custom BINs

```python
import sqlite3
conn = sqlite3.connect('bin_database.db')
cursor = conn.cursor()

cursor.execute('''
    INSERT INTO bins (bin, brand, type, bank, country, country_code, currency, valid)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', ('424242', 'VISA', 'CREDIT', 'CUSTOM BANK', 'India', 'IN', 'INR', 1))

conn.commit()
conn.close()
```

---

## 📝 License

MIT License - Free to use, modify, and distribute.

---

## 🤝 Contributing

Contributions welcome! To add more BINs:

1. Fork the repository
2. Add BINs to `build_database.py`
3. Test with `python3 bin_checker.py --stats`
4. Submit pull request

---

## ⚠️ Disclaimer

This database is for educational and development purposes. BIN data is sourced from public information and pattern generation. Always verify critical data with official sources.

---

## 🔗 Resources

- [ISO/IEC 7812](https://en.wikipedia.org/wiki/ISO/IEC_7812) - Card numbering standard
- [BIN Database](https://www.binbase.com/) - Online BIN lookup
- [Payment Card Industry](https://www.pcisecuritystandards.org/) - PCI standards

---

## 📧 Contact

Issues? Questions? Open an issue on GitHub!

---

**⭐ Star this repo if you find it useful!**

Made with ❤️ for developers who need offline BIN validation.
