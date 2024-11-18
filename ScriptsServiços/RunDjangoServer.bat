@echo off
cd C:\Users\WNB\Documents\ChatBot

call venv\Scripts\activate.bat

cd C:\Users\WNB\Documents\ChatBot\Project

python manage.py runserver 0.0.0.0:8000
pause
