from django.urls import path
from appone import views



urlpatterns=[
              path('all/',views.all_view),
              path('add/',views.add_view)
]
