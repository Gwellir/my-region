#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py fill_db
python manage.py loaddata fixtures/fixture