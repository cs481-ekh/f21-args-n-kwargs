"A point-by-point set of instructions
on how to install/
update the project into
production"

- mkdir WebSearchableEquipmentDatabase/fileUploads
- change permissions on filesUploads to allow the apache server write permission (on RedHat check SELinux roles)
- Create the python virtual environment:
  -     python3 -m venv ./venv
- Activate the virtual environment
  -     . venv/bin/activate
- Install all python packages
  -     pip install -r requirements.txt
- Create migrations
  -     python WebSearchableEquipmentDatabase/manage.py makemigrations accounts equipment
- Apply migrations
  -     python WebSearchableEquipmentDatabase/manage.py migrate
- Edit settings.py to add email credentials for smtp sends
- Make sure the Google account security is set to allow logins from insecure apps
  - myaccount.google.com/security
- Create superuser account
  -       cd WebSearchableEquipmentDatabase
          python manage.py shell
          shell> from accounts.models import Account
          shell> Account.objects.create_superuser(email="myaccount@gmail.com", password="mypassword")
- Start server
  -        python WebSearchableEquipmentDatabase/manage.py runserver