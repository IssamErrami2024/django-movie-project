# Install Celery: pip install celery
CELERY_BROKER_URL = 'amqp://localhost'  # Adjust if needed for a different broker

# Celery Configuration
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# Schedule ranking update task every 5 minutes (300 seconds)
CELERY_BEAT_SCHEDULE = {
    'update_movie_rankings': {
        'task': 'movies.tasks.update_movie_rankings',
        'schedule': crontab(minute='*/5'),  # Every 5 minutes
    },
}
# ... other settings ...

INSTALLED_APPS = [
    # ... your other apps ...
    'cenimaApp',  # Your app with models and serializers
    'rest_framework',  # Optional, for Django REST Framework features
    'ninja',  # Django Ninja for building APIs
]

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dj_cenima',
        'USER': 'admin',
        'PASSWORD': '',
    }
}

# Django Ninja settings (optional, for more complex API needs)
#NINJA_EXTRA_dependencies = {
   # 'db': get_db,   Optional, if using Ninja with Django database integration
#}

# Django REST Framework settings (optional, for custom API behavior)
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # Adjust permissions as needed
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',  # Use JSON for API responses
    ]
}