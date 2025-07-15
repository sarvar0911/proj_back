from django.contrib import admin
from .models import (
    Course,
    University,
    StudyMode,
    ClassTimeOption,
    CourseRegistration,
)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(StudyMode)
class StudyModeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(ClassTimeOption)
class ClassTimeOptionAdmin(admin.ModelAdmin):
    list_display = ('label',)
    search_fields = ('label',)


@admin.register(CourseRegistration)
class CourseRegistrationAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'preferred_name',
        'email',
        'current_city_or_region',
        'created_at',
        'wants_premium',
        'apply_for_merit_discount',
    )
    list_filter = (
        'wants_premium',
        'apply_for_merit_discount',
        'preferred_study_mode',
        'created_at',
    )
    search_fields = (
        'full_name',
        'preferred_name',
        'email',
        'telegram_handle',
        'heard_about_us',
    )
    filter_horizontal = ('course', 'intended_universities', 'ideal_class_times')
    readonly_fields = ('created_at',)
