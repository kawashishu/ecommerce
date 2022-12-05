release: python manage.py migrate 
web: gunicorn ecommerce.wsgi --log-file - 
worker: celery -A ecommerce.celery worker --loglevel=info --beat