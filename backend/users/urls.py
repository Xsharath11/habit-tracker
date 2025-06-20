from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SignupViewSet, LoginViewSet, LogoutViewSet

router = DefaultRouter()
router.register(r'signup', viewset=SignupViewSet, basename="signup")
router.register(r'login', viewset=LoginViewSet, basename="login")
router.register(r'logout', viewset=LogoutViewSet, basename="logout")

urlpatterns = router.urls
