from django.db import models
from django.contrib.auth.models import User

# Create your models here.
HABIT_STATUS = ["DONE", "NOT-DONE"]

class Habit(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField()

    def __str__(self):
        return self.name

class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=HABIT_STATUS, default="NOT-DONE")

    def __str__(self):
        return f"{self.habit.name} - {self.date} - {self.status}"
