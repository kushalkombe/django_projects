from django.urls import path
from apptwo import views as v1
from appone import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
              path('courseview/',v1.admin_courseview,name='course'),
              path('batchview/',v1.admin_batchview,name='batch'),
              path('facultyview/',v1.admin_facultyview,name='faculty'),
              path('studentview/',v1.admin_studentview,name='student'),
              path('adminactivity/',v1.admin_activity),
              path('ccreate/',v1.CourseCreate.as_view()),
              path('cupdate/<int:pk>/', v1.CourseUpdate.as_view(), name='cupdate'),
              path('cdelete/<int:pk>/', v1.CourseDelete.as_view(), name='cdelete'),
              path('bcreate/',v1.BatchCreate.as_view()),
              path('bupdate/<int:pk>/', v1.BatchUpdate.as_view(), name='bupdate'),
              path('bdelete/<int:pk>/', v1.BatchDelete.as_view(), name='bdelete'),
              path('fcreate/',v1.FacultyCreate.as_view()),
              path('fupdate/<int:pk>/', v1.FacultyUpdate.as_view(), name='fupdate'),
              path('fdelete/<int:pk>/', v1.FacultyDelete.as_view(), name='fdelete'),
              path('screate/',v1.AdstudentCreate.as_view()),
              path('supdate/<int:pk>/', v1.StudentUpdate.as_view(), name='supdate'),
              path('sdelete/<int:pk>/', v1.StudentDelete.as_view(), name='sdelete'),

]
