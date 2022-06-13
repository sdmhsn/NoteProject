from django.urls import path, include
from rest_framwarok.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('login', LoginViewSet, basename='login')
router.register('register', RegisterViewSet, basename='register')
router.register('category', CategoryViewSet, basename='register')
router.register('note', NoteViewSet, basename='note')

urlpatterns = [
    path('', include(router.urls)),
]
