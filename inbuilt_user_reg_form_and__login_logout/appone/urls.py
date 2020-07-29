from django.urls import path
from appone import views

urlpatterns=[
               path('home/',views.user_registration),
               path('success/',views.success_view),
               path('add/',views.add_image)
]
