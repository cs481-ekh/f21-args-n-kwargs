from django.shortcuts import render


def index(request):
    return render(request, 'equipment/base.html')

def dataTable(request):
    return render(request, 'equipment/dataTable.html')