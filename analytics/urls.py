from django.urls import path
from .import views

urlpatterns = [
    path('analise/', views.analise, name='analise'),
    path('analise_copy/', views.future_values, name='analise-copy'),
]
