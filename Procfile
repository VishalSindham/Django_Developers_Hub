release : python manage.py migrate
web: gunicorn devsearch.wsgi --log-file - --bind 0.0.0.0:$PORT
python:  python manage.py collectstatic –noinput && python manage.py runserver
