from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    return render(request, 'equipment/base.html')


def dataTable(request):
    context = {'dataTable': True, 'user': request.user}
    return render(request, 'equipment/dataTable.html', context)


def upload_csv(request):
    error = False
    if not request.user.is_superuser:
        return redirect('home')
    if request.POST:
        file = request.POST.get('file', False)
        if not file:
            messages.error(request, "Please select a file to be uploaded.")
            error = True
        elif not str(file).lower().endswith('.csv'):
            messages.error(request, "File must be a .csv")
            error = True

        # TODO: actual parsing logic
        if not error:
            messages.success(request, "File uploaded successfully!")

    # Used to dynamically set the nav bar link to active.
    # Example: <a class="nav-item nav-link {% if upload_csv %}active{% endif %}">Upload File</a>
    context = {'upload_csv': True, 'user': request.user}
    return render(request, 'equipment/uploadCSV.html', context)
