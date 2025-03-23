#!/bin/bash

echo "Установка Selenium и необходимых библиотек для Linux..."

# Проверка, установлен ли Python3
if ! command -v python3 &> /dev/null; then
    echo "Python3 не найден. Устанавливаем..."
    sudo apt update
    sudo apt install -y python3 python3-pip
else
    echo "Python3 уже установлен."
fi

# Проверка, установлен ли pip
if ! command -v pip3 &> /dev/null; then
    echo "pip3 не найден. Устанавливаем..."
    sudo apt install -y python3-pip
else
    echo "pip3 уже установлен."
fi

# Установка Selenium и других библиотек
echo "Устанавливаем Selenium, requests и pytest..."
pip3 install selenium requests pytest

# Установка веб-драйвера для Chrome (если нужно)
echo "Устанавливаем ChromeDriver..."
if ! command -v google-chrome &> /dev/null; then
    echo "Google Chrome не установлен. Устанавливаем..."
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo apt install -y ./google-chrome-stable_current_amd64.deb
    rm google-chrome-stable_current_amd64.deb
fi

# Установка ChromeDriver
CHROME_VERSION=$(google-chrome --version | awk '{print $3}' | cut -d '.' -f 1)
CHROMEDRIVER_VERSION=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION)
wget https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/
rm chromedriver_linux64.zip

echo "Установка завершена!"