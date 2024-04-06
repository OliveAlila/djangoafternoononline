from django.shortcuts import render

from django.http import HttpResponse


def karibu(request):
  return HttpResponse("<h1>Karibu to Django class</h1>")

def about(request):
  return render(request, template_name='about.html'),


def contact(request):
  return render(request, template_name='contact.html')


def services(request):
  return render(request, template_name='services.html')

 def gallery(request):
    return render(request, template_name='gallery.html')
