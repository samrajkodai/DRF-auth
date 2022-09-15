from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Teacher(models.Model):
    name=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    phoneno=models.IntegerField(max_length=11)


class Student(models.Model):
    name=models.CharField(max_length=20,unique=True)
    std=models.IntegerField()
    sub1_mark=models.IntegerField()
    sub2_mark=models.IntegerField()
    sub3_mark=models.IntegerField()
    sub4_mark=models.IntegerField()
    sub5_mark=models.IntegerField()
    Rank=models.IntegerField()

    REQUIRED_FIELDS= ['name',
            'std',
            'sub1_mark',
            'sub2_mark',
            'sub3_mark',
            'sub4_mark',
            'sub5_mark',
            'Rank']

    