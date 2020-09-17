release: python manage.py makemigrations api --no-input
release: python manage.py migrate --no-input
release: python manage.py fake
web: gunicorn theater_project.wsgi