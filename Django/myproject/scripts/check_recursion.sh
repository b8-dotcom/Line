#!/bin/sh
echo "Running recursion detector..."
python scripts/recursion_detector.py my_app/views.py
if [ $? -ne 0 ]; then
    echo "Recursion detected. Please fix the recursive calls before committing."
    exit 1
fi
