from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name="home"),
    path('values/', views.insert_value, name="insert-values"),
]
