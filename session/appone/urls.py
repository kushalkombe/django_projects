from django.urls import path
from appone import views

urlpatterns=[
               path('name/',views.name_view),
               path('age/',views.process_name_view),
               path('gfname/',views.process_age_view),
               path('result/',views.process_gfname_view)
]
