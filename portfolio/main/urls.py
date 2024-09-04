from django.urls import path
from . import views
from .views import download_resume
from .views import contact_view
urlpatterns=[
    path("",views.home,name='home'),
    path('download-resume/', download_resume, name='download_resume'),
    path('contact/', contact_view, name='contact'),


]



