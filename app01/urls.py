#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
#----------------------------------------------
# Copyright (python) 
# FileName: urls.py
# Version: 0.0.2
# Author : baiyang
# LastChange: 2017/7/19  10:27
# Desc:
# History:
#--------------------------------------------
"""
"""django_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from app01.views.views import hello
from app01.views.task import *

urlpatterns = [
    url(r'hello/$', hello, name="hello"),
    url(r'^tasks/$', task_list, name='task_list'),
    # url(r'^tasks/$', views.TaskList.as_view(), name='task_list'),
    url(r'^tasks/easy/$',TaskListCreate.as_view(), name='task_list'),
    url(r'^tasks/(?P<pk>[0-9]+)$', task_detail, name='task_detail'),

]
