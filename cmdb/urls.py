"""hdopsm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from views.host_view import *
from views.itsystem_view import *

urlpatterns = [
    # itsystem URL
    url(r'^itsystem/import/$', itsystem_import_view, name='itsystem_import'),
    url(r'^itsystem/list/$', itsystem_list_view, name='itsystem_list'),
    url(r'^itsystem/search/$', itsystem_search_view, name='itsystem_search'),
    url(r'^itsystem/delete/$', itsystem_delete_view, name='itsystem_delete'),
    url(r'^itsystem/detail/(?P<id>[0-9]+)/$', itsystem_detail_view, name='itsystem_detail'),
    url(r'^itsystem/update/(?P<id>[0-9]+)/$', itsystem_update_view, name='itsystem_update'),
    url(r'^itsystem/template/$', itsystem_template_view, name='itsystem_template'),
    url(r'^itsystem/export/$', itsystem_export_view, name='itsystem_export'),
    # host URL
    url(r'^host/list/$', host_list_view, name='host_list'),
    url(r'^host/import/$', host_import_view, name='host_import'),
    url(r'^host/delete/$', host_delete_view, name='host_delete'),
    url(r'^host/detail/(?P<id>[0-9]+)/$', host_detail_view, name='host_detail'),
    url(r'^host/update/(?P<id>[0-9]+)/$', host_update_view, name='host_update'),
    url(r'^host/template/$', host_template_view, name='host_template'),
    url(r'^host/export/$', host_export_view, name='host_export'),
    url(r'^host/search/$', host_search_view, name='host_search'),
]
