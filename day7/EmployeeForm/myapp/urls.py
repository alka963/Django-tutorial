from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.home),
    path('add/', views.add),
    path('findall/', views.Findall),
    path('update/', views.update),
    path('delete/', views.delete),
]