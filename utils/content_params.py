#!/usr/bin/env python
# encoding: utf-8


def format_content_dict(params, object_list, p, objects, page_range, current_page, show_first, show_end):
    params['object_list'] =object_list
    params['p'] = p
    params['objects'] = objects
    params['page_range'] = page_range
    params['current_page'] = current_page
    params['show_first'] = show_first
    params['show_end'] = show_end
    return params
