# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from models import Tabla
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context

# Create your views here.

@csrf_exempt
def serverCSS(request,recurso):

    verb = request.method
    #Indicar plantilla
    plantilla = get_template('index.html')

    if verb == 'GET':
        if recurso == '':
            titulo = "Insertar en el put con el siguiente formato:"
            formato = "nombre,fecha(YYYY-MM-DD)"
            c = Context({'titulo': titulo, 'parrafo':formato})
            #Renderizar
            renderizado = plantilla.render(c)      
            return HttpResponse(renderizado)
        else:
            try:
                record = Tabla.objects.get(nombre = recurso)
                #Definir el contexto
                fecha = ("Fecha de "+recurso+"= "+ str(record.fecha))
                c = Context({'contenidoCSS': fecha})
                #Renderizar
                renderizado = plantilla.render(c)
                return HttpResponse(renderizado)

            except Tabla.DoesNotExist:
                return HttpResponseNotFound("Page not found: %s." % recurso)

    elif verb == 'PUT':
        cuerpo = request.body.split(',')
        name = cuerpo[0]
        date = cuerpo[1]
        db = Tabla(nombre = name,fecha = date)
        db.save()
        return HttpResponse('<h1>Nombre y fecha almacenados</h1>')

@csrf_exempt
def server(request,recurso):
    verb = request.method
    #Indicar plantilla
    plantilla = get_template('index.html')

    if verb == 'GET':
        if recurso == '':
            titulo = "Insertar en el put con el siguiente formato:"
            formato = "nombre,fecha(YYYY-MM-DD)"
            c = Context({'titulo': titulo, 'parrafo':formato})
            #Renderizar
            renderizado = plantilla.render(c)      
            return HttpResponse(renderizado)
        else:
            try:
                record = Tabla.objects.get(nombre = recurso)
                #Definir el contexto
                fecha = ("Fecha de "+recurso+"= "+ str(record.fecha))
                c = Context({'contenido': fecha})
                #Renderizar
                renderizado = plantilla.render(c)
                return HttpResponse(renderizado)

            except Tabla.DoesNotExist:
                return HttpResponseNotFound("Page not found: %s." % recurso)

    elif verb == 'PUT':
        cuerpo = request.body.split(',')
        name = cuerpo[0]
        date = cuerpo[1]
        db = Tabla(nombre = name,fecha = date)
        db.save()
        return HttpResponse('<h1>Nombre y fecha almacenados</h1>')


def css(request):
    
    #Indicar plantilla
    plantilla = get_template('css/main.css')
    #Definir el contexto
    c = Context({'contenidoCSS':"hola"})
    #Renderizar
    renderizado = plantilla.render(c)

    return HttpResponse(renderizado, content_type = 'text/css')
