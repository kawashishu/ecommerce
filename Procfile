release: python manage.py migrate 
web: gunicorn ecommerce.wsgi --log-file - 
worker: celery -A tasks worker --loglevel=info --beat