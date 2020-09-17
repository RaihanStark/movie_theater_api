release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
release: python manage.py fake
web: gunicorn theater_project.wsgi