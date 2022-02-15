# Installation
* mkdir drf
* cd drf
* mkvirtualenv drf / pipenv shell /
* pip install django django-debug-toolbar djangorestframework drf-yasg
* django-admin startproject config .
* python manage.py startapp users
* python manage.py runserver


## First step - django rest framework, debug_toolbar, swagger, CustomUser
#### settings.py
```python
INSTALLED_APPS = [...
    'debug_toolbar',
    'rest_framework',
    'drf_yasg',
                  
    'users.apps.UsersConfig',
...]
MIDDLEWARE = [...
    'debug_toolbar.middleware.DebugToolbarMiddleware', ...]
INTERNAL_IPS = [
    "127.0.0.1",]
AUTH_USER_MODEL = 'users.CustomUser'
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]}
```
* changes in: config/urls.py, users/models.py, users/admin.py
#### terminal:
- python manage.py makemigrations
- python manage.py migrate

## User: dj-rest-auth
- https://dj-rest-auth.readthedocs.io/en/latest/installation.html
####terminal
- pip install dj-rest-auth==
#### settings.py
```python
INSTALLED_APPS = [...
    'dj_rest_auth',
    'rest_framework.authtoken', ...]

REST_FRAMEWORK = {...
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication', 
    ],}
```
* changes in config/urls.py
- endpoint: v1/api/dj-rest-auth/login/ logout/  password/
- no endpoint for registration


