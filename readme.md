## Some useful commands
- create virtual environment```python -m venv .venv```
- enter to venv ```.venv\Scripts\activate```
- list installed libraries (package.json) ```pip freeze > requirements.txt```
- come out of venv ```deactivate```
- install dependencies ```pip install -r requirements.txt```

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

- flow
![django-flow](./django-flow.png)

#### Run server
```
python manage.py runserver
```


#### Create super user (admin)
```
python manage.py createsuperuser
```

#### Migrate (moves the user model to admin model)
```
python manage.py makemigrations
python manage.py migrate
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