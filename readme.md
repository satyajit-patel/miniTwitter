## Some useful commands
- create virtual environment```python -m venv .venv```
- enter to venv ```.venv\Scripts\activate```
- to list installed libraries ```pip freeze > requirements.txt```
- to come out of venv ```deactivate```
- to install dependencies ```pip install -r requirements.txt```

#### Install django
```
pip install django
```

#### Start project
```
django-admin startproject miniTwitter
```

- move inside project
```
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

#### Migrate (if any changes made to DB)
```
python manage.py makemigrations
python manage.py migrate
```

#### Create super user (admin)
```
python manage.py createsuperuser
```

### settings.py

- imports
```
import os
```

#### Media configuration

- install pillow
```
pip install pillow
```

- set media
```
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

#### Static configuration
- set static
```
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

### urls.py
- imports
```
from django.conf import settings
from django.conf.urls.static import static
```

- link settings (attach at the end of urlpatterns list)
```
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
```