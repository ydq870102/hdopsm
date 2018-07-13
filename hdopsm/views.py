#!/usr/bin/env python
# encoding: utf-8

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response



def index(request):
    '''
    @首页
    '''
    return render_to_response('index.html', locals())

def index2(request):
    '''
    @首页
    '''
    return render_to_response('index2.html')