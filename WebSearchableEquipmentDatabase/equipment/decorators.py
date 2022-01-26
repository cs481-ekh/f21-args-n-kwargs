from django.http import HttpResponse


def allowed_groups(allowed_groups=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if request.user.is_superuser or group in allowed_groups:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You aren't authorized to view this page")
        return wrapper_func
    return decorator