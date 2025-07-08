from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HabitLogViewset, HabitViewSet

router = DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habit')
router.register(r'habitlogs', HabitLogViewset, basename='habitlog')

urlpatterns = router.urls

