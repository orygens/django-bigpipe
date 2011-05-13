#!/usr/bin/python
# -*- coding: utf-8 -*-

# django-bipipe
# https://github.com/orygens/django-bigpipe

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 Orygens contato@orygens.com

from django.conf import settings
from django.template import RequestContext
from django.template.loader import render_to_string

class Pagelet(object):
    """
    Simple parent class for all pagelets. Only implements rendering.
    """

    js = []
    css = []
    context = {}
    is_last = False
    content_template = None

    def __init__(self, id, request, **kwargs):
        self.id = id
        self.request = request
        
        cls = self.__class__
        for key, value in kwargs.iteritems():
          if not hasattr(cls, key):
              raise TypeError(u'%s() received an invalid keyword %r' %
                  (cls.__name__, key))

          setattr(self, key, value)

    def get_context_data(self):
        """
        Simple context generating. Subclasses must override this method
        to add more data to the context passed to template.
        """

        return self.context

    def get_js_resources(self):
        return self._get_static_resources('js')

    def get_css_resources(self):
        return self._get_static_resources('css')

    def _get_static_resources(self, name):
        return map(lambda s: '%s%s' % (settings.MEDIA_URL, s),
            getattr(self, name))

    def get_html_content(self):
        content = ''

        if self.content_template:
            content = render_to_string(self.content_template,
                self.get_context_data(), RequestContext(self.request))

        return content

    def render(self):
        return render_to_string('bigpipe/pagelet.html',
            {'pagelet': self}, RequestContext(self.request))

