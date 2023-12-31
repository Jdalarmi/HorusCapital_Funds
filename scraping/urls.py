from django.urls import path
from . import views

urlpatterns = [
    path('fiis/', views.start, name='start-fiis')
]
