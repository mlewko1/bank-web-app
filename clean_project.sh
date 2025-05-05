#!/bin/bash

echo "=== Rozpoczynanie czyszczenia projektu ==="

# 1. Deaktywacja venv jeśli aktywny
if type deactivate &> /dev/null; then
    echo "Deaktywacja środowiska wirtualnego..."
    deactivate
fi

# 2. Usuwanie venv
if [ -d "venv" ]; then
    echo "Usuwanie środowiska wirtualnego..."
    rm -rf venv
fi

# 3. Usuwanie plików tymczasowych
echo "Czyszczenie plików tymczasowych..."
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f -name "*.pyc" -delete
find . -type f -name "*.pyo" -delete

# 4. Usuwanie plików projektu (opcjonalne)
read -p "Czy chcesz usunąć wszystkie pliki projektu? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo "Usuwanie plików projektu..."
    rm -rf bank_app/
    rm -f requirements.txt
    rm -f db.sqlite
fi

echo "=== Czyszczenie zakończone ==="