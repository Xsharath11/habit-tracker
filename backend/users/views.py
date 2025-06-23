from django.contrib.auth import logout
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import SignupSerializer, LoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication 
from rest_framework import status

class SignupViewSet(ViewSet):
    def create(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token':token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginViewSet(ViewSet):
    def create(self, request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutViewSet(ViewSet):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def create(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response({"detail": "Successfully Logged Out"}, status=status.HTTP_200_OK)
