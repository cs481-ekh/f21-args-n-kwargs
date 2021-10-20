#!/bin/bash
python -m pip install --upgrade pip || exit $?
pip install -r requirements.txt || exit $?
cd WebSearchableEquipmentDatabase || exit $?
python manage.py makemigrations || exit $?
python manage.py test || exit $?