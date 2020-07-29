from django.urls import path
from lion import views
urlpatterns=[
               path('one/',views.a),
               path('two/',views.b),
               path('three/',views.c)
]
