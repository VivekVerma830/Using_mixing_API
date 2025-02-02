from.models import *
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']