from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.app_homepage, name='app_homepage')
]
