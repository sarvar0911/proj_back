from rest_framework import serializers
from .models import CourseRegistration, Course


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRegistration
        fields = '__all__'
