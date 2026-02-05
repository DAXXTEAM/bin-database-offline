# 💳 BIN Database - Offline Checker

**Complete offline BIN (Bank Identification Number) database with 9,600+ verified entries.**

No API required! Fast, local SQLite database with Python lookup tools.

---

## 🚀 Features

✅ **9,639 BINs** - Verified bank identification numbers  
✅ **100% Offline** - No API keys or internet required  
✅ **Fast Lookup** - SQLite database with indexes  
✅ **40+ Countries** - Worldwide coverage  
✅ **Multiple Brands** - Visa, Mastercard, Amex, RuPay, Discover, Maestro, UnionPay  
✅ **Rich Data** - Bank name, country, currency, phone, website  
✅ **JSON Export** - Easy integration  
✅ **Search Options** - By BIN, brand, country, bank  

---

## 📊 Database Stats

| Metric | Count |
|--------|-------|
| **Total BINs** | 9,639 |
| **Countries** | 40+ |
| **Brands** | 7 (Visa, MC, Amex, RuPay, Discover, Maestro, UnionPay) |
| **Banks** | 200+ major banks |

### Coverage by Country

🇺🇸 USA • 🇮🇳 India • 🇬🇧 UK • 🇨🇦 Canada • 🇯🇵 Japan • 🇧🇷 Brazil • 🇦🇺 Australia • 🇫🇷 France • 🇩🇪 Germany • 🇪🇸 Spain • 🇲🇽 Mexico • 🇷🇺 Russia • 🇨🇳 China • 🇰🇷 South Korea • 🇸🇬 Singapore • 🇦🇪 UAE • 🇸🇦 Saudi Arabia • And 30+ more!

---

## ⚡ Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/DAXXTEAM/bin-database-offline.git
cd bin-database-offline
```

### 2. Use Checker

```bash
# Lookup a BIN
python3 bin_checker.py 510377

# Search by brand
python3 bin_checker.py --brand mastercard

# Search by country
python3 bin_checker.py --country IN

# Get statistics
python3 bin_checker.py --stats
```

---

## 📖 Usage Examples

### Basic Lookup

```bash
$ python3 bin_checker.py 511416
```

**Output:**
```
======================================================================
💳 BIN: 511416
======================================================================
Brand:        MASTERCARD
Type:         DEBIT
Level:        PLATINUM
Bank:         ICICI BANK LIMITED
Country:      India (IN)
Currency:     INR
Valid:        ✅ Yes
======================================================================
```

### Python Integration

```python
from bin_checker import BINChecker

# Initialize
checker = BINChecker()

# Lookup BIN
result = checker.lookup('510377')
print(f"Bank: {result['bank']}")
print(f"Country: {result['country']}")

# Search by country
india_cards = checker.search_by_country('IN')

# Get stats
stats = checker.get_stats()
print(f"Total BINs: {stats['total']:,}")

# Close connection
checker.close()
```

---

## 🐍 Python Import

```python
from bin_checker import BINChecker

# Context manager (auto-close)
with BINChecker() as checker:
    result = checker.lookup('460223')
    if result:
        print(f"{result['brand']} - {result['bank']}")
```

---

## 📁 File Structure

```
bin-database-offline/
├── README.md              # This file
├── bin_checker.py         # Lookup tool
├── bin_database.db        # SQLite database (9,639 BINs)
├── build_database.py      # Database builder
├── test.sh                # Test script
└── .gitignore            # Git ignore rules
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

## 💳 Supported Brands

- **VISA** - 2,200+ BINs
- **MASTERCARD** - 2,200+ BINs
- **AMERICAN EXPRESS** - 1,600+ BINs
- **RUPAY** - 1,650+ BINs (India domestic)
- **DISCOVER** - 900+ BINs
- **MAESTRO** - 1,600+ BINs
- **UNIONPAY** - 100+ BINs (China)

---

## 🌍 Major Banks Included

### India 🇮🇳
- State Bank of India (SBI)
- HDFC Bank
- ICICI Bank
- Axis Bank
- Kotak Mahindra Bank
- And 50+ more

### USA 🇺🇸
- JPMorgan Chase
- Bank of America
- Wells Fargo
- Citibank
- Capital One
- And 100+ more

### Worldwide 🌍
- HSBC (UK)
- Barclays (UK)
- Scotiabank (Canada)
- Santander (Spain/Brazil)
- And 100+ international banks

---

## 🔧 Advanced Features

### Bulk Lookup

```python
bins = ['510377', '511416', '534444']
for bin_num in bins:
    result = checker.lookup(bin_num)
    print(f"{bin_num}: {result['bank'] if result else 'Not found'}")
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
''', ('999999', 'VISA', 'CREDIT', 'MY BANK', 'India', 'IN', 'INR', 1))

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
2. Add BINs to database
3. Test with `python3 bin_checker.py --stats`
4. Submit pull request

---

## ⚠️ Disclaimer

This database is for educational and development purposes. BIN data is sourced from public information. Always verify critical data with official sources.

---

## 🔗 Resources

- [ISO/IEC 7812](https://en.wikipedia.org/wiki/ISO/IEC_7812) - Card numbering standard
- [Payment Card Industry](https://www.pcisecuritystandards.org/) - PCI standards

---

## 📧 Contact

Issues? Questions? Open an issue on GitHub!

---

## 🔄 Changelog

### v1.1.0 (Latest)
- ✅ Added 563 new BINs
- ✅ Total: 9,639 BINs
- ✅ 40+ countries coverage
- ✅ 200+ banks included

### v1.0.0
- 🎉 Initial release
- ✅ 9,093 BINs
- ✅ 4 countries

---

**⭐ Star this repo if you find it useful!**

Made with ❤️ for developers who need offline BIN validation.
