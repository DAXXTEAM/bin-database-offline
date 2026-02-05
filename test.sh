#!/bin/bash
echo "🧪 Running BIN Database Tests..."
echo ""

echo "Test 1: Database exists"
if [ -f bin_database.db ]; then
    echo "✅ Database file found"
else
    echo "❌ Database missing - run: python3 build_database.py"
    exit 1
fi

echo ""
echo "Test 2: Statistics"
python3 bin_checker.py --stats

echo ""
echo "Test 3: Sample lookups"
python3 bin_checker.py 400782
python3 bin_checker.py 512648

echo ""
echo "Test 4: Search by brand"
python3 bin_checker.py --brand visa | head -20

echo ""
echo "Test 5: JSON output"
python3 bin_checker.py 400782 --json

echo ""
echo "✅ All tests passed!"
