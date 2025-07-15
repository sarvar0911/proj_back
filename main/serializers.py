from rest_framework import serializers
from .models import (
    Course,
    University,
    StudyMode,
    ClassTimeOption,
    CourseRegistration,
)


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "name"]


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ["id", "name"]


class StudyModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyMode
        fields = ["id", "name"]


class ClassTimeOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassTimeOption
        fields = ["id", "label"]


class CourseRegistrationSerializer(serializers.ModelSerializer):
    course = CourseListSerializer(many=True, read_only=True)
    intended_universities = UniversitySerializer(many=True, read_only=True)
    preferred_study_mode = StudyModeSerializer(read_only=True)
    ideal_class_times = ClassTimeOptionSerializer(many=True, read_only=True)

    course_ids = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), many=True, write_only=True, source='course'
    )
    intended_university_ids = serializers.PrimaryKeyRelatedField(
        queryset=University.objects.all(), many=True, write_only=True, source='intended_universities'
    )
    preferred_study_mode_id = serializers.PrimaryKeyRelatedField(
        queryset=StudyMode.objects.all(), write_only=True, source='preferred_study_mode'
    )
    ideal_class_time_ids = serializers.PrimaryKeyRelatedField(
        queryset=ClassTimeOption.objects.all(), many=True, write_only=True, source='ideal_class_times'
    )

    class Meta:
        model = CourseRegistration
        fields = [
            'id',
            'full_name', 'preferred_name', 'email', 'telegram_handle',
            'date_of_birth', 'current_city_or_region', 'current_education_level',

            'course', 'course_ids',
            'intended_universities', 'intended_university_ids',
            'preferred_study_mode', 'preferred_study_mode_id',
            'ideal_class_times', 'ideal_class_time_ids',

            'top_goal', 'apply_for_merit_discount', 'heard_about_us', 'wants_premium',

            'notes',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at']
