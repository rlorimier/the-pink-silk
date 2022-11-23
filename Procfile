release: python manage.py makemigrations && python manage.py migrate
web: gunicorn pink_silk.wsgi:application