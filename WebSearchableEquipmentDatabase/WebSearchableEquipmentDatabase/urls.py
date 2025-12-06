"""WebSearchableEquipmentDatabase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from accounts import views as auth_views
from WebSearchableEquipmentDatabase import views


site_patterns = [
    path('', views.landing, name='home'),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    # This will put every link in the equipment.urls.py file under equipment/{methodName}
    path('', include('equipment.urls')),

]



if settings.DEBUG:
    site_patterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    site_patterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Force static files serving
if not settings.DEBUG:
    site_patterns += [
        re_path(r'static/(?P<path>.*)$', serve, {
            'document_root': settings.STATIC_ROOT,
        }),
        re_path(r'media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]


urlpatterns = [
    path(f'{settings.HTML_ROOT}/', include(site_patterns)) # changes site root based on global variable in settings.py
]
