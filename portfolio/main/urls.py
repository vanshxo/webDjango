from django.urls import path
from . import views
from .views import download_resume

urlpatterns=[
    path("",views.home,name='home'),
    path('download-resume/', download_resume, name='download_resume'),



]




