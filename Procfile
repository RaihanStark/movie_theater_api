release: python manage.py makemigrations api --no-input
release: python manage.py migrate api zero --no-input
release: python manage.py migrate api --no-input
release: python manage.py fake
web: gunicorn theater_project.wsgi