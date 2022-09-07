web: gunicorn devsearch.wsgi --log-file -
python manage.py collectstatic --noinput
manage.py runserver
manage.py migrate
