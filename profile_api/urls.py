from django.urls import path
from  profile_api import  views

urlpatterns = [
    path('hello-view', views.HelloApiView.as_view()),
    path('homies-view', views.HelloApiView.as_view()),
    path('bros-view', views.HelloApiView.as_view()),
]