#### Commands
```
python -m venv .venv
.venv\Scripts\activate
pip install django
pip freeze > requirements.txt
deactivate
pip install -r requirements.txt
```

#### Start project
```
django-admin startproject miniTwitter
cd  miniTwitter
```

#### Start app
```
python manage.py startapp tweet
```

#### Run server
```
python manage.py runserver
```

#### Migrate
```
python manage.py makemigrations
python manage.py migrate
```

#### Create super user (admin)
```
python manage.py createsuperuser
```

### settings.py
#### Media configuration
```
import os

pip install pillow

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

#### Static configuratin
```
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static)]
```

### urls.py
```
from django.conf import settings
from django.conf.urls.static import static

# attach at the end of urlpatterns list
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
```