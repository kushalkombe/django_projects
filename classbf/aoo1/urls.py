from django.urls import path
from aoo1 import views
urlpatterns=[
             path('add/',views.Add.as_view()),
             path('fetch/',views.Fetch.as_view()),
             path('delete/<int:id>/',views.Delete.as_view()),
             path('update/<int:id>/',views.Update.as_view())
]
