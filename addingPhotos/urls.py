from . import views
from django.urls import path

urlpatterns = [
    path('', views.adding_photos_page, name='adding photo page')
]