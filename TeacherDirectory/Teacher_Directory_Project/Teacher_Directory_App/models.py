from django.db import models


# Create your models here.


class Teacher_Directory(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(null=True, blank=True)
    email = models.EmailField(unique=True, max_length=100)
    phone_number = models.CharField(max_length=25, null=True, default=0)
    room_number = models.CharField(max_length=100)
    subjects = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
