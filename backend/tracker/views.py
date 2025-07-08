from django.shortcuts import render, get_object_or_404    
from rest_framework import viewsets, permissions
from rest_framework.views import Response
from .models import Habit, HabitLog
from .serializers import HabitSerializer, HabitLogSerializer
from tracker import serializers

# Create your views here.
class HabitViewSet(viewsets.ViewSet):
    serializer_class = HabitSerializer 

    def list(self, request):
        habits = Habit.objects.filter(user=request.user)
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = HabitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class HabitLogViewset(viewsets.ViewSet):
    serializer_class = HabitLogSerializer

    def list(self, request):
        habitlogs = HabitLog.objects.filter(habit__user=request.user)
        serializer = HabitLogSerializer(habitlogs, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = HabitLogSerializer(data=request.data)
        if serializer.is_valid():
            # habit = serializer.validated_data.get("habit")
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
