#!/usr/bin/env python
# encoding: utf-8

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from hdopsm.models import *
from django.db.models import Q
from hdopsm.common import pages
from utils.importaction import ImportAction
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def itsystem_import(request):
    if request.method == "POST":
        import_object = ImportAction(request)
        data_list = import_object.get_data()
        for data in data_list:
            print data
    else:
        keyword = request.GET.get('keyword', '')
        object_list = Itsystem.objects.all().order_by('itsystem_name')
        if keyword:
            object_list = Itsystem.objects.filter(Q(itsystem_name=keyword))

        object_list, p, objects, page_range, current_page, show_first, show_end = pages(object_list, request)

        return render_to_response('index2.html', locals())
