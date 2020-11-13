from django.urls import path
from firstapp import views

urlpatterns=[
               path('home/',views.user_registration),
               path('success/',views.success_view),
               path('add/',views.Add.as_view()),
               path('delete/<int:id>/',views.Delete.as_view()),
               path('update/<int:id>/',views.Update.as_view()),




]
