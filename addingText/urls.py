from . import views
from django.urls import path

urlpatterns = [
    path('', views.adding_text_page, name='adding text page'),
]