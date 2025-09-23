from django.urls import path
from my_web.views import home, about, contact,projects

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('projects/', projects, name='projects'),
]