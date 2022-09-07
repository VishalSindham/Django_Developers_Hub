release : python manage.py migrate
web: gunicorn devsearch.wsgi --log-file -
python:  python manage.py collectstatic –noinput && python manage.py runserver 
