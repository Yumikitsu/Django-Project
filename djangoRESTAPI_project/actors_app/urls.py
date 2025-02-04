from . import views
from django.urls import path

urlpatterns = [
    path('', views.ActorsList.as_view()),
    path('actor/<int:pk>', views.ActorByID.as_view()),
]