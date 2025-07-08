from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Habit(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class HabitLog(models.Model):
    class Status(models.TextChoices):
        DONE = "Done"
        NOT_DONE = "NOT_DONE"

    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.NOT_DONE)

    def __str__(self):
        return f"{self.habit.name} - {self.date} - {self.status}"
