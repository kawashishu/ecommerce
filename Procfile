release: python manage.py migrate 
web: gunicorn ecommerce.wsgi --log-file - 
django: python manage.py loaddata fixtures/Category.json 
django: python manage.py loaddata fixtures/Customer.json 
django: python manage.py loaddata fixtures/Product.json