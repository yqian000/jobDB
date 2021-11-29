from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('job/', views.JobViewOrCreate.as_view(), name='job'),
    path('job/<int:pk>/', views.JobUpdateOrDelete.as_view()),
    path('job/main/', views.main),
    path('job/postjob/', views.postjob),
    path('job/myposts', views.myposts),
]