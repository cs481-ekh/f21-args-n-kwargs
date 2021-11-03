import csv
import os
import uuid

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Equipment
from .models import Center_Lab
from .models import Category
from .forms import EquipmentForm
from .decorators import allowed_groups


# The C in CRUD
@login_required
@allowed_groups(allowed_groups=['faculty'])
def create_equipment(request):
    form = EquipmentForm()
    if request.POST:
        form = EquipmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    # TODO: @michael update with actual template
    return render(request, 'equipment/equipmentForm.html', context)


def index(request):
    return render(request, 'equipment/base.html')


def filter_data(request, locations, categories):
    context = {'dataTable': True,
               'user': request.user,
               'show_controls': request.user.groups.all().filter(name="faculty").exists(),
               'data': Equipment.objects().all().filter(location__in=locations).filter(category__in=categories)
               }
    return render(request, 'equipment/dataTable.html', context)


def data_table(request):
    equipmentObjects = Equipment.objects.all()
    if request.user.groups.all().filter(name="student"):
        equipmentObjects = equipmentObjects.exclude(permission="faculty")
    elif request.user.groups.all().filter(name="guest"):
        equipmentObjects = equipmentObjects.filter(permission="guest")
    context = {'dataTable': True,
               'user': request.user,
               'show_controls': request.user.groups.all().filter(name="faculty").exists(),
               'data': equipmentObjects,
               'categories': Category.CATEGORY,
               'form': EquipmentForm
               }
    return render(request, 'equipment/dataTable.html', context)


def save_file(file):
    directory = 'fileUploads/'
    file_name = uuid.uuid4()
    path = directory + str(file_name) + '.csv'
    with open(path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return path


def delete_file(path):
    os.remove(path)
    return


def upload_csv(request):
    error = False
    processed_file = False
    path = ''
    if request.POST:
        category_map = {
            "A": Category.processing,
            "B": Category.structural,
            "C": Category.chemical,
            "D": Category.mechanical,
            "E": Category.electrical,
            "F": Category.thermal,
            "O": Category.other,
        }
        file = request.FILES['file']
        if not file:
            messages.error(request, "Please select a file to be uploaded.")
            error = True
        elif not str(file).lower().endswith('.csv'):
            messages.error(request, "File must be a .csv")
            error = True

        if not error:
            try:
                path = save_file(file)
                processed_file = True
                with open(path) as f:
                    reader = csv.reader(f)
                    for row in reader:
                        obj, created = Equipment.objects.get_or_create(
                            name=row[0],
                            model=row[1],
                            manufacturer=row[2],
                            year=row[3],
                            pi=row[4],
                            contact=row[5],
                            location=row[7],
                            description=row[8],
                            url=row[10],
                            permission=Equipment.guest,  # TODO: update accordingly
                        )

                        Center_Lab.objects.create(
                            center_lab_label=row[6],
                            equipment=obj
                        ),

                        # This bit of code handles multiple categories for a piece of equipment
                        sanitized = row[9].replace(" ", "").upper()
                        split = sanitized.split(',')
                        for val in split:
                            Category.objects.create(
                                label=category_map[val],
                                equipment=obj
                            )

                    messages.success(request, "File uploaded successfully!")
            except Exception:
                error = True

    if error:
        messages.error(request, "There was an error processing your file.")
    if processed_file:
        delete_file(path)
    context = {'upload_csv': True, 'user': request.user}
    return render(request, 'equipment/uploadCSV.html', context)


def testing(request):
    form = EquipmentForm()
    if request.method == "POST":
        form = EquipmentForm(request.POST)
        if form.is_valid():
            pass
    content = {'form': form}
    return render(request, 'equipment/testingEquipmentForm.html', content)
