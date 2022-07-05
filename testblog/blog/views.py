#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2020 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
Authors: zhuziyi
Date:    2022/07/01
Comment: 第一个 blog views，瞎写吧
"""

from django.shortcuts import render
from django.http import HttpResponse
from . import models


# def index(request):
#     return HttpResponse('天行健，君子自强不息！')


def index(request):
    article = models.Article.objects.get(pk=1)

    return render(request, 'blogpage/index.html', {'article': article})


def hello(request):
    return HttpResponse('hello world！')


def basketball(request):
    # article = models.Article.objects.get(pk=1)
    return render(request, 'blogpage/basketball.html')

