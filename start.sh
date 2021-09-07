python3 -m venv ./venv
pip install -r requirements.txt
python WebSearchableEquipmentDatabase/manage.py migrate
python WebSearchableEquipmentDatabase/manage.py runserver
