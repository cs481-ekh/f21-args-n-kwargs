#!/bin/bash python
python -m pip install --upgrade pip || exit $?
pip install -r requirements.txt || exit $?
cd WebSearchableEquipmentDatabase || exit $?
python manage.py makemigrations || exit $?

import experiment.export.tests || exit $?
python manage.py test || exit $?