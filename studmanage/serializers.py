from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    subjects = serializers.JSONField(required=True)
    class Meta:
        model = Student
        fields = '__all__'
