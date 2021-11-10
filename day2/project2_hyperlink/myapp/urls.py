from django.urls import path
from . import views
urlpatterns = [
    path('first/',views.home),
    path('f1/',views.first),
    path('f2/', views.second),
    path('f3/', views.third),
]