pip install -r requirements.txt
python manage.py migrate
# run celery worker and beat
celery -A ecommerce worker -l info
celery -A ecommerce beat -l info