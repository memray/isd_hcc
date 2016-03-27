#coding: utf-8
from django.shortcuts import render

def index(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q'].encode('utf-8')
    else:
        message = '你提交了空表单'
    return render(request, 'index.html', {'message': message})


# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse(u"Hello world!")
#     string = u'Welcome to Jungle!'
#     return render(request, 'index.html', {'string': string})
