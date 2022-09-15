from dataclasses import fields
from rest_framework import serializers
from .models import Teacher,Student


class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=[
            'name',
            'subject',
            'phoneno'
        ]

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=[
            'id',
            'name',
            'std',
            'sub1_mark',
            'sub2_mark',
            'sub3_mark',
            'sub4_mark',
            'sub5_mark',
            'Rank'
        ]