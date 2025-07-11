from rest_framework import serializers
from .models import CourseRegistration, Course


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "name"]


class CourseRegistrationSerializer(serializers.ModelSerializer):
    course = CourseListSerializer(many=True, read_only=True)
    course_ids = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), many=True, write_only=True, source='course'
    )

    class Meta:
        model = CourseRegistration
        fields = ['id', 'full_name', 'email', 'course', 'course_ids', 'notes', 'created_at']
        read_only_fields = ['created_at']