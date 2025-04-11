@echo off
echo Creating Python virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing pip...
python -m ensurepip --default-pip

echo Installing requirements...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo Setup complete! You can now run the services:
echo python products/app.py
echo python parts/app.py 