from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here.

def juguetes(request):
    return render(request,'templatesApp/juguetes.html')

def index (request):
    return render(request,'templatesApp/index.html')

def ropa (request):
    return render(request,'templatesApp/ropa.html')

def info_usuario (request):
    doc_externo = open('C:/Users/holas/Dropbox/Mi PC (LAPTOP-DOMFHH14)/Desktop/Inacap/programacion back end/django_evaluacion_1/plantillas/templatesApp/userinfotemplate.html')
    plt = Template(doc_externo.read())
    doc_externo.close()
    data = {
        'id': '123',
        'nombre' : 'Omar Ramirez',
        'email': 'omar@omar.cl'
    }
    ctx = Context(data)
    docu = plt.render(ctx)
    return HttpResponse(docu)