"""
URL configuration for Analytics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
cv c f    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
    path('api_accountant/', include('api_accountant.urls')),
    path('api_admin/', include('api_admin.urls')),
    path('api_librarian/', include('api_librarian.urls')),
    path('api_parent/', include('api_parent.urls')),
    path('api_student/', include('api_student.urls')),
    path('api_super_admin/', include('api_super_admin.urls')),
    path('api_teacher/', include('api_teacher.urls')),
    # path('parent/', include('parent.urls')),
    path('accountant/', include('web_accountant.urls')),
    path('web_admin/', include('web_admin.urls')),
    path('app/', include('web_app.urls')),
    path('librarian/', include('web_librarian.urls')),
    path('parents/', include('web_parents.urls')),
    path('student/', include('web_student.urls')),
    path('super_admin/', include('web_super_admin.urls')),
    path('teacher/', include('web_teacher.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)