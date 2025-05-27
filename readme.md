#### Commands
```
python -m venv .venv
.venv\Scripts\activate
pip install django
django-admin startproject miniTwitter
cd  miniTwitter
python manage.py startserver
pip freeze > requirements.txt
deactivate
pip install -r requirements.txt
```