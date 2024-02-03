from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TimesheetEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)
    activity = models.CharField(max_length=20)
    ACTIVITY_CHOICES = [
        ('reading', 'Đọc sách'),
        ('football', 'Đá bóng'),
        ('gaming', 'Chơi Game'),
        ('swimming', 'Bơi lội'),
        ('badminton', 'Cầu Lông'),
        ('studying', 'Học bài'),
    ]

    activity = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)

    # GENDER_CHOICES = [
    #     ('reading_books', 'Đọc sách'),
    #     ('playing_soccer', 'Đá bóng'),
    #     ('playing_games', 'Chơi Game'),
    #     ('swimming', 'Bơi lội'),
    #     ('badminton', 'Cầu Lông'),
    #     ('studying', 'Học bài'),
    # ]
    # gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
