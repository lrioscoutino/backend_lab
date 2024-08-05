from django.shortcuts import render
from django.http import HttpResponse
from users.models import Subject


def first_view(request):
    cadena = "Hola Desde django"
    # Codigo python
    # Consultar una base de datos
    # consumir la herramienta
    return HttpResponse(cadena)


def second_view(request):
    subjects = Subject.objects.filter(is_active=True)
    number_list = [2, 4, 5, 6, 8, 34]
    context = {
        "subjects": subjects,
        "name": "Luis Rios",
        "age": 47,
        "number_list": number_list
    }
    return render(request, "base.html", context=context)
