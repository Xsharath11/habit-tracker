from rest_framework import serializers
from .models import Habit, HabitLog

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ["id",'user', 'name', 'created_at']
        read_only_fields = ['id','user', 'created_at']

class HabitLogSerializer(serializers.ModelSerializer):
    habit_name = serializers.CharField(source='habit.name', read_only=True)
    class Meta:
        model = HabitLog
        fields = ['id', 'habit', 'habit_name','date','status']
        read_only_fields = ['id']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=HabitLog.objects.all(),
                fields=['habit', 'date'],
                message = "Log for this day already exists."
            )
        ]

    def validate(self, attrs: dict) -> dict:
        habit = attrs.get("habit")
        log_date = attrs.get("date")

        # Prevent logging before habit creation
        if habit and log_date and log_date < habit.created_at:
            raise serializers.ValidationError("Log date cannot be before habit created at date")

        return attrs


