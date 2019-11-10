from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('main/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def menu(request):
    template = loader.get_template('main/menu.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def restroom(request):
    template = loader.get_template('main/restroom.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
