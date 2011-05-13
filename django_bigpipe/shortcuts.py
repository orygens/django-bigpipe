#!/usr/bin/python
# -*- coding: utf-8 -*-

# django-bipipe
# https://github.com/orygens/django-bigpipe

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 Orygens contato@orygens.com

from django.template.loader import render_to_string
from django.template import RequestContext
from django.http import HttpResponse

def render_pagelets(request, template_name='base.html',
    pagelets=[], extra_context=[]):
    return HttpResponse(stream_pagelets(request,
      template_name, pagelets, extra_context))

def stream_pagelets(request, template_name, pagelets, extra_context):
    """
    Render the basic page structure and flush each pagelet response.
    """
    yield render_to_string(template_name, extra_context,
        context_instance=RequestContext(request))

    for pagelet in pagelets:
        yield pagelet.render()

    yield '</body></html>\n'

