# 🚀 Setup Guide

Complete installation and usage instructions for BIN Database Offline.

---

## Installation

### Method 1: Download Release (Recommended)

1. Go to [Releases](https://github.com/yourusername/bin-database-offline/releases)
2. Download latest `bin-database-offline.zip`
3. Extract and run:

```bash
unzip bin-database-offline.zip
cd bin-database-offline
python3 bin_checker.py --stats
```

### Method 2: Git Clone

```bash
git clone https://github.com/yourusername/bin-database-offline.git
cd bin-database-offline
python3 bin_checker.py --stats
```

### Method 3: Build from Scratch

```bash
git clone https://github.com/yourusername/bin-database-offline.git
cd bin-database-offline
rm bin_database.db  # Remove pre-built database
python3 build_database.py  # Build fresh database
python3 bin_checker.py --stats
```

---

## Quick Test

After installation, test with:

```bash
# Check stats
python3 bin_checker.py --stats

# Lookup sample BINs
python3 bin_checker.py 400782  # SBI Visa
python3 bin_checker.py 512648  # Axis Mastercard
python3 bin_checker.py 378282  # Amex
```

---

## Usage Examples

### 1. Basic Lookup

```bash
python3 bin_checker.py 424242
```

### 2. Search Operations

```bash
# Find all Visa cards
python3 bin_checker.py --brand visa

# Find all Indian cards
python3 bin_checker.py --country IN

# Find HDFC Bank cards
python3 bin_checker.py --bank HDFC
```

### 3. JSON Output

```bash
# Get JSON for integration
python3 bin_checker.py 400782 --json > result.json
```

### 4. Bulk Operations

Create `bins.txt`:
```
400782
512648
378282
```

Run:
```bash
while read bin; do
  python3 bin_checker.py $bin
done < bins.txt
```

---

## Python Integration

### Example Script

Create `my_app.py`:

```python
#!/usr/bin/env python3
from bin_checker import BINChecker

# Initialize
checker = BINChecker()

# Lookup BIN
bin_num = input("Enter BIN: ")
result = checker.lookup(bin_num)

if result:
    print(f"Bank: {result['bank']}")
    print(f"Country: {result['country']}")
    print(f"Brand: {result['brand']}")
else:
    print("BIN not found")

# Close
checker.close()
```

Run:
```bash
python3 my_app.py
```

---

## Troubleshooting

### Database not found

If you see `unable to open database file`:

```bash
# Build database
python3 build_database.py
```

### Permission denied

```bash
chmod +x bin_checker.py build_database.py
```

### Python version

Requires Python 3.6+:

```bash
python3 --version  # Should be 3.6 or higher
```

---

## Advanced Usage

### Export to CSV

```bash
sqlite3 bin_database.db <<EOF
.headers on
.mode csv
.output bins_export.csv
SELECT * FROM bins;
.quit
EOF
```

### Add Custom BINs

```python
import sqlite3

conn = sqlite3.connect('bin_database.db')
cursor = conn.cursor()

# Add your BIN
cursor.execute('''
    INSERT OR REPLACE INTO bins 
    (bin, brand, type, bank, country, country_code, currency, valid)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', (
    '999999',
    'VISA',
    'CREDIT',
    'MY CUSTOM BANK',
    'India',
    'IN',
    'INR',
    1
))

conn.commit()
conn.close()
```

### Web API Wrapper

Create `api.py`:

```python
from flask import Flask, jsonify
from bin_checker import BINChecker

app = Flask(__name__)
checker = BINChecker()

@app.route('/bin/<bin_number>')
def get_bin(bin_number):
    result = checker.lookup(bin_number)
    if result:
        return jsonify(result)
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(port=5000)
```

Run:
```bash
pip3 install flask
python3 api.py
```

Access: http://localhost:5000/bin/400782

---

## Performance Tips

1. **Keep database on SSD** for faster lookups
2. **Use indexes** (already created by default)
3. **Close connections** after use
4. **Batch operations** when processing multiple BINs

---

## Updates

To get latest BIN data:

```bash
git pull origin main
python3 build_database.py
```

---

## Support

- 📖 Read [README.md](README.md)
- 🐛 [Report issues](https://github.com/yourusername/bin-database-offline/issues)
- 💬 [Discussions](https://github.com/yourusername/bin-database-offline/discussions)

---

**Happy BIN checking! 💳**
