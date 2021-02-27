from django.shortcuts import render
from django.http import HttpResponse

def adding_photos_page(request):
    return HttpResponse('page for adding photos')

