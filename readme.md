#### Commands
```
python -m venv .venv
.venv\Scripts\activate
pip install django
django-admin startproject miniTwitter
cd  miniTwitter
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
pip freeze > requirements.txt
deactivate
pip install -r requirements.txt
```