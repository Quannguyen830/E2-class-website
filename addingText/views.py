from django.shortcuts import render
from django.http import HttpResponse

def adding_text_page(request):
    return HttpResponse('page for adding text')
