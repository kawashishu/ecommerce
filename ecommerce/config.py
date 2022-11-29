import os

timezone =  'Asia/Ho_Chi_Minh'   #It is important to set a timezone if you want celery beat to work
broker_url = os.environ.get('REDIS_URL')    
result_backend = os.environ.get('REDIS_URL')
broker_pool_limit = None

beat_schedule = {
                'get_notification': {
            'task': 'schedule.tasks.get_notification',
            'schedule': 10.0,
                },
            'get_api_currency': {
            'task': 'schedule.tasks.get_api_currency',
            'schedule': 10,
            },
}