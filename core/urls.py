from django.urls import path
from . import views

urlpatterns = [
    path('directions/', views.GetAllDirections.as_view()),
    path('doctors/', views.GetAllDoctors.as_view()),
    path('doctors/<int:pk>/', views.GetDoctor.as_view({'get': 'list'}))
]
