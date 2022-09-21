from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here.

def juguetes(request):
    data = {
        'titulo' : 'Juguetes Django',
        'imagen_1': '/static/images/juguetes/1.jfif',
        'descripcion_1': 'Juguete pelea de boxeo robot modelo 1980',
        'imagen_2': '/static/images/juguetes/2.jfif',
        'descripcion_2': 'T-rex 15cm de altura',
        'imagen_3': '/static/images/juguetes/3.jfif',
        'descripcion_3': 'Peluche Picachu',
        
    }
    return render(request,'templatesApp/productos.html',data)

def index (request):
    return render(request,'templatesApp/index.html')

def ropa (request):
    data = {
        'titulo' : 'Juguetes Django',
        'imagen_1': '/static/images/ropa/1.jfif',
        'descripcion_1': 'Pantalones Negros hombre',
        'imagen_2': '/static/images/ropa/2.jfif',
        'descripcion_2': 'Poleron adidas mujer',
        'imagen_3': '/static/images/ropa/3.jfif',
        'descripcion_3': 'Jardinera mujer',
        
    }
    return render(request,'templatesApp/productos.html',data)

def info_usuario (request):
    docu = """
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
        </head>
        <body class="container">
            <div class="alert alert-info display-1 text-center">
                <img src="/static/images/django.png" width="100px">
                <h1>Django Shop</h1>
            </div>
            
            <div class="row">
                <h1 class="col">Id Usuario: 123 </h1>
                <h1 class="col">Nombre Usuario: Omar Ramirez</h1>
                <h1 class="col">Correo Usuario: omar@omar.cl</h1>
            </div>

            <img src="/static/images/personaje.jpg" width="300px" >
            <div class="col-1"><a href="/" class="btn p-3 btn-info w-100">Volver</a></div>

        </body>
        </html>
    """
    return HttpResponse(docu)