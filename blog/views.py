# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import post

# Create your views here.
def post_list(request):
    posts = post.objects.all()
    return render(request, 'blog/post_list.html', {'posts' : posts})
