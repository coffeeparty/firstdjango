# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from posts.models import Record #capital letter because class always starts with capital letter. When you create this you save it and then on your webapp you can see the POSTS
admin.site.register(Record)

# Register your models here.
