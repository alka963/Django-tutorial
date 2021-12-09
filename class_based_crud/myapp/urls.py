from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.Home.as_view()),
    path('add/', views.AddRecord.as_view()),
    path('update/<int:pk>/', views.UpdateRecord.as_view()),
    path('delete/<int:pk>/', views.DeleteRecord.as_view()),
]
