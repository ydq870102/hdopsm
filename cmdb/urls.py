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
from views.sysdevice_view import *
from views.itsystem_view import *
from views.room_view import *
from views.zone_view import *
from views.process_view import *
from views.database_view import *


urlpatterns = [
    # itsystem URL
    url(r'^itsystem/import/$', itsystem_import_view, name='itsystem_import'),
    url(r'^itsystem/list/$', itsystem_list_view, name='itsystem_list'),
    url(r'^itsystem/search/$', itsystem_search_view, name='itsystem_search'),
    url(r'^itsystem/delete/$', itsystem_delete_view, name='itsystem_delete'),
    url(r'^itsystem/detail/(?P<id>[0-9]+)/$', itsystem_detail_view, name='itsystem_detail'),
    url(r'^itsystem/related/(?P<id>[0-9]+)/$', itsystem_related_view, name='itsystem_related'),
    url(r'^itsystem/record/(?P<id>[0-9]+)/$', itsystem_record_view, name='itsystem_record'),
    url(r'^itsystem/alarm/(?P<id>[0-9]+)/$', itsystem_alarm_view, name='itsystem_alarm'),
    url(r'^itsystem/update/(?P<id>[0-9]+)/$', itsystem_update_view, name='itsystem_update'),
    url(r'^itsystem/template/$', itsystem_template_view, name='itsystem_template'),
    url(r'^itsystem/export/$', itsystem_export_view, name='itsystem_export'),
    # sysdevice URL
    url(r'^sysdevice/list/$', sysdevice_list_view, name='sysdevice_list'),
    url(r'^sysdevice/import/$', sysdevice_import_view, name='sysdevice_import'),
    url(r'^sysdevice/delete/$', sysdevice_delete_view, name='sysdevice_delete'),
    url(r'^sysdevice/detail/(?P<id>[0-9]+)/$', sysdevice_detail_view, name='sysdevice_detail'),
    url(r'^sysdevice/related/(?P<id>[0-9]+)/$', sysdevice_related_view, name='sysdevice_related'),
    url(r'^sysdevice/record/(?P<id>[0-9]+)/$', sysdevice_record_view, name='sysdevice_record'),
    url(r'^sysdevice/alarm/(?P<id>[0-9]+)/$', sysdevice_alarm_view, name='sysdevice_alarm'),
    url(r'^sysdevice/update/(?P<id>[0-9]+)/$', sysdevice_update_view, name='sysdevice_update'),
    url(r'^sysdevice/template/$', sysdevice_template_view, name='sysdevice_template'),
    url(r'^sysdevice/export/$', sysdevice_export_view, name='sysdevice_export'),
    url(r'^sysdevice/search/$', sysdevice_search_view, name='sysdevice_search'),
    # room URL
    url(r'^room/list/$', room_list_view, name='room_list'),
    url(r'^room/import/$', room_import_view, name='room_import'),
    url(r'^room/delete/$', room_delete_view, name='room_delete'),
    url(r'^room/detail/(?P<id>[0-9]+)/$', room_detail_view, name='room_detail'),
    url(r'^room/related/(?P<id>[0-9]+)/$', room_related_view, name='room_related'),
    url(r'^room/record/(?P<id>[0-9]+)/$', room_record_view, name='room_record'),
    url(r'^room/alarm/(?P<id>[0-9]+)/$', room_alarm_view, name='room_alarm'),
    url(r'^room/update/(?P<id>[0-9]+)/$', room_update_view, name='room_update'),
    url(r'^room/template/$', room_template_view, name='room_template'),
    url(r'^room/export/$', room_export_view, name='room_export'),
    url(r'^room/search/$', room_search_view, name='room_search'),
    # zone URL
    url(r'^zone/list/$', zone_list_view, name='zone_list'),
    url(r'^zone/import/$', zone_import_view, name='zone_import'),
    url(r'^zone/delete/$', zone_delete_view, name='zone_delete'),
    url(r'^zone/detail/(?P<id>[0-9]+)/$', zone_detail_view, name='zone_detail'),
    url(r'^zone/related/(?P<id>[0-9]+)/$', zone_related_view, name='zone_related'),
    url(r'^zone/record/(?P<id>[0-9]+)/$', zone_record_view, name='zone_record'),
    url(r'^zone/alarm/(?P<id>[0-9]+)/$', zone_alarm_view, name='zone_alarm'),
    url(r'^zone/update/(?P<id>[0-9]+)/$', zone_update_view, name='zone_update'),
    url(r'^zone/template/$', zone_template_view, name='zone_template'),
    url(r'^zone/export/$', zone_export_view, name='zone_export'),
    url(r'^zone/search/$', zone_search_view, name='zone_search'),
    # process URL
    url(r'^process/list/$', process_list_view, name='process_list'),
    url(r'^process/import/$', process_import_view, name='process_import'),
    url(r'^process/delete/$', process_delete_view, name='process_delete'),
    url(r'^process/detail/(?P<id>[0-9]+)/$', process_detail_view, name='process_detail'),
    url(r'^process/related/(?P<id>[0-9]+)/$', process_related_view, name='process_related'),
    url(r'^process/record/(?P<id>[0-9]+)/$', process_record_view, name='process_record'),
    url(r'^process/alarm/(?P<id>[0-9]+)/$', process_alarm_view, name='process_alarm'),
    url(r'^process/update/(?P<id>[0-9]+)/$', process_update_view, name='process_update'),
    url(r'^process/template/$', process_template_view, name='process_template'),
    url(r'^process/export/$', process_export_view, name='process_export'),
    url(r'^process/search/$', process_search_view, name='process_search'),
    # database URL
    url(r'^database/list/$', database_list_view, name='database_list'),
    url(r'^database/import/$', database_import_view, name='database_import'),
    url(r'^database/delete/$', database_delete_view, name='database_delete'),
    url(r'^database/detail/(?P<id>[0-9]+)/$', database_detail_view, name='database_detail'),
    url(r'^database/related/(?P<id>[0-9]+)/$', database_related_view, name='database_related'),
    url(r'^database/record/(?P<id>[0-9]+)/$', database_record_view, name='database_record'),
    url(r'^database/alarm/(?P<id>[0-9]+)/$', database_alarm_view, name='database_alarm'),
    url(r'^database/update/(?P<id>[0-9]+)/$', database_update_view, name='database_update'),
    url(r'^database/template/$', database_template_view, name='database_template'),
    url(r'^database/export/$', database_export_view, name='database_export'),
    url(r'^database/search/$', database_search_view, name='database_search'),
]
