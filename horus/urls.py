from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name="home"),
    path('values/', views.insert_value, name="insert-values"),
    path('user_login/', views.user_login, name="user-login"),
    path('logout_user/', views.logout_user, name='logout-user'),
    path('delete_chart/', views.delete_chartjs, name='delete-chart'),
]
