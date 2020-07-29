from django.urls import path
from first import views

urlpatterns = [
    path('all/', views.all_view),
    path('delete/<int:id>/', views.Delete.as_view()),
    path('update/<int:id>/', views.Update.as_view()),
    path('add/', views.Add.as_view()),
]
