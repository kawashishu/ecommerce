release: python manage.py migrate 
web: gunicorn ecommerce.wsgi --log-file - 
celeryd: celery -A ecommerce.tasks worker --loglevel=info --beat