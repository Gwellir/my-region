#!/bin/sh

python manage.py migrate
# python manage.py fill_db
python manage.py loaddata fixtures/fixture_26032021