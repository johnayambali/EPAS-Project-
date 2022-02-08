from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='projectListing-home'),
    path('profile/', views.profile, name='projectListing-profile'),
    path('applications/', views.applications, name='projectListing-applications'),
]

