"""isd_hcc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from hcc import views as hcc_views
urlpatterns = [
    url(r'^$', hcc_views.index),
    url(r'^get_all/', hcc_views.get_all),
    url(r'^get_group1/', hcc_views.get_group1),
    url(r'^get_group2/', hcc_views.get_group2),
    url(r'^get_group3/', hcc_views.get_group3),
    url(r'^admin/', admin.site.urls),
]
