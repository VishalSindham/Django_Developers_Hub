release : python manage.py migrate
web: gunicorn devsearch.wsgi
python: python manage.py runserver
python: python manage.py collectstatic
