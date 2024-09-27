# players/urls.py
from django import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from django.contrib import admin
from django.urls import path

from players.views import CoachLoginView, CoachLogoutView, YourPlayerView

urlpatterns = [
    path('admin/', admin.site.urls), 
]

router = DefaultRouter()
router.register(r'players', YourPlayerView, basename='player')  

urlpatterns = [
    path('', include(router.urls)),
    path('coach/login/', CoachLoginView.as_view(), name='coach-login'),
    path('coach/logout/', CoachLogoutView.as_view(), name='coach-logout'),
]
