from django.urls import path
from . import views

urlpatterns = [
    path('fiis/', views.start, name='start-fiis'),
    path('new_fund/', views.get_fund, name= 'get-fund'),
]
