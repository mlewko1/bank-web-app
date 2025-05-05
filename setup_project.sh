#!/bin/bash

# Konfiguracja
PROJECT_NAME="bank_app"
VENV_DIR="venv"
REQUIREMENTS="requirements.txt"

echo "=== Rozpoczynanie konfiguracji projektu ${PROJECT_NAME} ==="

# 1. Sprawdź czy Python 3 jest dostępny
if ! command -v python3 &> /dev/null
then
    echo "Python 3 nie jest zainstalowany. Zainstaluj go przed kontynuowaniem."
    exit 1
fi

# 2. Utwórz środowisko wirtualne
echo "Tworzenie środowiska wirtualnego..."
python3 -m venv ${VENV_DIR}
if [ $? -ne 0 ]; then
    echo "Błąd podczas tworzenia venv!"
    exit 1
fi

# 3. Aktywuj venv
echo "Aktywowanie venv..."
source ${VENV_DIR}/bin/activate

# 4. Uaktualnij pip
echo "Aktualizacja pip..."
pip install --upgrade pip

# 5. Instalacja zależności
if [ -f "${REQUIREMENTS}" ]; then
    echo "Instalowanie zależności..."
    pip install -r ${REQUIREMENTS}
else
    echo "Plik ${REQUIREMENTS} nie istnieje. Instalowanie podstawowych zależności..."
    pip install flask flask-sqlalchemy flask-login
fi

# 6. Inicjalizacja projektu
echo "Tworzenie struktury projektu..."
mkdir -p ${PROJECT_NAME}/{models,routes,services,templates,static}


echo "=== Konfiguracja zakończona pomyślnie! ==="
echo "Aby aktywować środowisko: source ${VENV_DIR}/bin/activate"
echo "Aby uruchomić aplikację: python3 run.py"