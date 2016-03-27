#coding: utf-8
from django.shortcuts import render

def index(request):
    string = u'Welcome to Jungle!'
    return render(request, 'index.html', {'string': string})


# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse(u"Hello world!")
