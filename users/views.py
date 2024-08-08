from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from users.models import Subject


def first_view(request):
    cadena = "Hola Desde django"
    # Codigo python
    # Consultar una base de datos
    # consumir la herramienta
    return HttpResponse(cadena)


def initial_view(request):
    return render(request, "base.html")


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


def subjects_view(request):
    subjects = Subject.objects.all()
    context = {
        "subjects": subjects
    }
    return render(request, "subjects.html", context=context)


def add_subjects_view(request):
    if request.method == 'POST':
        subject = Subject()
        subject.name = request.POST['name']
        subject.description = request.POST['description']
        subject.save()
        return redirect(reverse_lazy("subjects-view"))
    context = {}
    return render(request, "form.html", context=context)


def update_subjects_view(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    if request.method == 'POST':
        subject.name = request.POST['name']
        subject.description = request.POST['description']
        subject.save()
        return redirect(reverse_lazy("subjects-view"))
    context = {
        "subject": subject
    }
    return render(request, "form.html", context=context)
