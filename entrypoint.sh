#!/bin/bash

# For sqlite db and cron.logs (later)
mkdir -p /app
python manage.py migrate
python manage.py collectstatic --clear --noinput
python manage.py runserver 0.0.0.0:8000
