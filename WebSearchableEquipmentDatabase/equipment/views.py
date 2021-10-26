import csv
import re

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
# from django.views.decorators.http
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
    return render(request, 'equipment/dataTable.html', context);


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


def upload_csv(request):
    error = False
    if not request.user.is_superuser:
        return redirect('home')
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
        regex = re.compile('[^A-Z]')  # Only allow uppercase alphabetic strings
        file = request.POST.get('file', False)
        if not file:
            messages.error(request, "Please select a file to be uploaded.")
            error = True
        elif not str(file).lower().endswith('.csv'):
            messages.error(request, "File must be a .csv")
            error = True

        with open(file) as f:
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
                for col in row[9]:
                    col = col.upper()  # Always uppercase
                    col = regex.sub('', col)  # Strip non-uppercase/non-alphabetic characters
                    Category.objects.create(
                        label=category_map[col],
                        equipment=obj
                    )

        if not error:
            messages.success(request, "File uploaded successfully!")
        else:
            messages.error(request, "There was an error processing your file.")

    # Used to dynamically set the nav bar link to active.
    # Example: <a class="nav-item nav-link {% if upload_csv %}active{% endif %}">Upload File</a>
    context = {'upload_csv': True, 'user': request.user}
    return render(request, 'equipment/uploadCSV.html', context)
