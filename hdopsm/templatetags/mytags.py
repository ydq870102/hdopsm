#! /usr/bin/env python
#  encoding: utf-8


from django import template
from hdopsm.models import Enum

register = template.Library()


@register.filter(name='enum_to_string')
def enum_to_string(num):
    if num == 0 or num is None:
        return '否'
    if num == 1:
        return '是'
