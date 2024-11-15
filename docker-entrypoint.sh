#!/bin/bash

echo "En attente de la base de donnée"
#./wait-for db:5432

echo "Collectstatic"
python manage.py collectstatic --no-input

echo "Execution des migrations"
python manage.py migrate

echo "Demarrage du serveur"
gunicorn --config gunicorn-cfg.py config.wsgi