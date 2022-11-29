release: python manage.py migrate 
web: gunicorn ecommerce.wsgi --log-file - 
celery: worker: celery -A tibController.tasks worker --loglevel=info --beat