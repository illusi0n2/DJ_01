from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Домашнее задание из урока DJ 01</h1>')

def first(request):
    return HttpResponse('<h1>Первая страница проекта</h1>')

def second(request):
    return HttpResponse('<h1>Вторая страница проекта</h1>')