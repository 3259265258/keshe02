"""TTT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.dom.expatbuilder import DOCUMENT_NODE
from xml.dom.minidom import Document
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,re_path
from operation import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('orm/',views.orm),
    path('add/',views.add),
    path('query/',views.query),
    path('select/',views.select),
    path('update/',views.update),
    path('delete/',views.delete),
    path('add_user_image/', views.add_user_image, name='add_user_image'),
    path('upload_handle/', views.upload_handle, name='upload_handle'),
    path('show_avatar/', views.show_avatar, name='show_avatar'),

  ]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
