from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.Registration),
    path('login/', views.Login),
    path('home/', views.home),
]
