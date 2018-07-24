#!/usr/bin/env python
# encoding: utf-8

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from models import *
from django.db.models import Q
from common import pages
from cmdb.models import *

def index(request):
    '''
    @首页
    '''
    return render_to_response('index.html', locals())

def index2(request):
    '''
    @首页
    '''
    keyword = request.GET.get('keyword', '')
    object_list = ItSystem.objects.all().order_by('itsystem_name')
    if keyword:
        object_list = ItSystem.objects.filter(Q(itsystem_name=keyword))

    object_list, p, objects, page_range, current_page, show_first, show_end = pages(object_list, request)
    msg = "ddsdadadas"

    return render_to_response('index2.html', locals())


def itsystem_del(request):
    '''
    @首页
    '''
    keyword = request.GET.get('keyword', '')
    object_list = ItSystem.objects.all().order_by('itsystem_name')
    if keyword:
        object_list = ItSystem.objects.filter(Q(itsystem_name=keyword))

    object_list, p, objects, page_range, current_page, show_first, show_end = pages(object_list, request)

    return render_to_response('index2.html', locals())
