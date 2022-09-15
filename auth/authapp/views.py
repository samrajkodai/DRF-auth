from rest_framework import mixins,generics
from .serializers import TeacherSerializers,StudentSerializers
from .models import Student, Teacher
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response


@permission_classes([IsAuthenticated])
class StudentInfo(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

        queryset=Student.objects.all()
        serializer_class=StudentSerializers

        def get(self,request,*args, **kwargs):
            return self.list(request,*args,**kwargs)


        def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)

@permission_classes([IsAuthenticated])
class Student(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):

        queryset = Student.objects.all()
        serializer_class = StudentSerializers

        def get(self, request, *args, **kwargs):
            return self.retrieve(request, *args, **kwargs)

        def put(self, request, *args, **kwargs):
            return self.update(request, *args, **kwargs)

        def delete(self, request, *args, **kwargs):
            return self.destroy(request, *args, **kwargs)


