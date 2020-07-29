from django.urls import path
from first import views

urlpatterns = [
    path('user/', views.user_registration),
    path("success/", views.success_view),
    path('add/', views.add_image),
    path('fetch/', views.img_fetch),
    path('login2/', views.login),
    path('logout/', views.logout),
]
