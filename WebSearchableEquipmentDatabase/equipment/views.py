import csv
import os
import uuid

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
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
            data = {
                'created': True
            }
            return JsonResponse(data)
    context = {'form': form}
    return render(request, 'equipment/equipmentForm.html', context)


def index(request):
    return render(request, 'equipment/base.html')


def filter_data(request):
    categories = request.GET.get('categories[]', '')
    locations = request.GET.get('locations[]', '')
    data = Equipment.objects.all()
    if locations and categories :#empty strings are falsy, so as long as they have data, go for it
        data = data.filter(equipment_center_lab__center_lab_label__in=locations.split(',')).filter(equipCat__label__in=categories.split(','))
    elif categories and not locations:
        data = data.filter(equipCat__label__in=categories.split(','))
    elif locations and not categories:
        data = data.filter(equipment_center_lab__center_lab_label__in=locations.split(','))

    if request.user.groups.all().filter(name="student"):
        data = data.exclude(permission="faculty")
    elif request.user.groups.all().filter(name="guest"):
        data = data.filter(permission="guest")
    context = {'dataTable': True,
               'user': request.user,
               'show_controls': request.user.groups.all().filter(name="faculty").exists(),
               'categories': Category.CATEGORY,
               'locations': Center_Lab.LOCATION,
               'form': EquipmentForm,
               'data': data.distinct(),
               'filter': True,
               'filteredCategories': categories,
               'filteredLocations': locations
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
               'locations': Center_Lab.LOCATION,
               'form': EquipmentForm,
               'home': True,
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


def get_item_by_id(request):
    if request.POST:
        group = request.user.groups.all()
        if not group or not group[0].name == "faculty":
            raise Exception("The action is not allowed for you")
        obj = Equipment.objects.get(id=request.POST.get('id'))
        obj.name = request.POST.get('name')
        obj.model = request.POST.get('model')
        obj.manufacturer = request.POST.get('manufacturer')
        obj.year = request.POST.get('year')
        obj.pi = request.POST.get('pi')
        obj.location = request.POST.get('location')
        obj.contact = request.POST.get('contact')
        obj.description = request.POST.get('description')
        obj.url = request.POST.get('url')
        obj.permission = request.POST.get('permission')
        obj.save()
        data = {'updated': True}
        return JsonResponse(data)
    id1 = request.GET.get('id', None)
    obj = Equipment.objects.get(id=id1)
    data = {
        'id': obj.id,
        'name': obj.name,
        'model': obj.model,
        'manufacturer': obj.manufacturer,
        'year': obj.year,
        'pi': obj.pi,
        'location': obj.location,
        'contact': obj.contact,
        'description': obj.description,
        'url': obj.url,
        'permission': obj.permission
    }
    return JsonResponse(data)


def delete_file(path):
    os.remove(path)
    return


@login_required
@allowed_groups(allowed_groups=['faculty'])
def upload_csv(request):
    processed_file = False
    path = ''
    last_line_parsed = ''
    headers = False
    context = {
        'upload_csv': True,
        'user': request.user,
        'show_controls': request.user.groups.all().filter(name="faculty").exists()
    }

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

        if request.POST.get('headers'):
            headers = True

        try:
            file = request.FILES['file']
        except Exception:
            messages.error(request, "Please select a file to be uploaded.")
            return render(request, 'equipment/uploadCSV.html', context)

        if not str(file).lower().endswith('.csv'):
            messages.error(request, "File must be a .csv")
            return render(request, 'equipment/uploadCSV.html', context)

        try:
            path = save_file(file)
            processed_file = True
            with open(path) as f:
                reader = csv.reader(f)
                if headers:
                    next(reader, None)
                for row in reader:
                    last_line_parsed = row
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

                    if row[6] != '':
                        Center_Lab.objects.create(
                            center_lab_label=row[6],
                            equipment=obj
                        ),

                    # This bit of code handles multiple categories for a piece of equipment
                    category_list = ['A', 'B', 'C', 'D', 'E', 'F', 'O']
                    sanitized = row[9].replace(" ", "").upper()
                    split = sanitized.split(',')
                    for val in split:
                        if val in category_list:
                            Category.objects.create(
                                label=category_map[val],
                                equipment=obj
                            )

                messages.success(request, "File uploaded successfully!")
        except Exception:
            messages.error(request, "An error occurred trying to parse the following line: " + str(last_line_parsed))

    if processed_file:
        delete_file(path)
    return render(request, 'equipment/uploadCSV.html', context)


def testing(request):
    form = EquipmentForm()
    if request.method == "POST":
        form = EquipmentForm(request.POST)
        if form.is_valid():
            pass
    content = {'form': form}
    return render(request, 'equipment/testingEquipmentForm.html', content)


def delete_equipment(request):
    id1 = request.GET.get('id', None)
    numDeleted = Equipment.objects.get(id=id1).delete() #Delete returns the number of rows deleted, which should be 1 if the item exists
    data = {
        'deleted': numDeleted, #This makes it so that the deleted flag is only set when something is actually deleted
    }
    return JsonResponse(data)
