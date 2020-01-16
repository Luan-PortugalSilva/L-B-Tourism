from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .templates import app
from .models import Tour, FeedBack

def home(request):
    feed_backs = FeedBack.objects.all()
    page = 'Home'
    template = loader.get_template('app/index.html')
    context = {
        'page': page,
        'feed_backs': feed_backs,
    }
    return HttpResponse(template.render(context, request))


def passeios(request):
    passeios = Tour.objects.all()
    page = 'Passeios'
    template = loader.get_template('app/passeios.html')
    context = {
        'page': page,
        'passeios': passeios,
    }
    return HttpResponse(template.render(context, request))


def contato(request):
    page = 'Contato'
    template = loader.get_template('app/contato.html')
    context = {
        'page': page,
    }
    return HttpResponse(template.render(context, request))

def values(request, id):
    try:
        tour = Tour.objects.get(pk=id)
    except Tour.DoesNotExist:
        raise Http404("Question does not exist")
    page = 'Valores'
    template = loader.get_template('app/values.html')
    context = {
        'page': page,
        'tour': tour,
    }
    return HttpResponse(template.render(context, request))