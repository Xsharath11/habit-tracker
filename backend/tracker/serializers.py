from rest_framework import serializers
from .models import Habit, HabitLog

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ["id",'user', 'name', 'created_at']
        read_only_fields = ['id','user', 'created_at']

class HabitLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitLog
        fields = ['id', 'habit','date','status']
        read_only_fields = ['id']

    def validate(self, attrs: dict) -> dict:
        habit = attrs.get("habit")
        log_date = attrs.get("date")

        # Prevent logging before habit creation
        if habit and log_date and log_date < habit.created_at:
            raise serializers.ValidationError("Log date cannot be before habit created at date")

        return attrs


