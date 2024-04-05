### Postgres DB setup

- Create a new local database

- Go to [sampledjango/settings.py] and update the following
  DATABASES = {
  'default': {
  'ENGINE': 'django.db.backends.postgresql',
  'NAME': 'test', # Database Name
  'USER': 'postgres',
  'PASSWORD': 'test',
  'HOST': '127.0.0.1',
  'PORT': '5432'
  }
  }

- Migrate
  python manage.py migrate

- Run server
  python manage.py runserver
