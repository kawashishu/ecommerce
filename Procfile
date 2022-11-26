release: python manage.py migrate 
web: gunicorn ecommerce.wsgi --log-file - 
celery: celery -A ecommerce.celery worker --pool=solo  -l info
celerybeat: celery -A ecommerce beat -l info