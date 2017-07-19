#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
#----------------------------------------------
# Copyright (python) 
# FileName: serializers.py
# Version: 0.0.2
# Author : baiyang
# LastChange: 2017/7/19  13:32
# Desc:
# History:
#--------------------------------------------
"""
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'completed', 'create_date')
