from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'course'
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class University(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'university'
        verbose_name = "University"
        verbose_name_plural = "Universities"


class StudyMode(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'study_mode'
        verbose_name = "Study Mode"
        verbose_name_plural = "Study Modes"


class ClassTimeOption(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label

    class Meta:
        db_table = 'class_time_option'
        verbose_name = "Class Time"
        verbose_name_plural = "Class Times"


class CourseRegistration(models.Model):
    # Basic Info
    full_name = models.CharField(max_length=255, null=True, blank=True)
    preferred_name = models.CharField(max_length=255, null=True, blank=True)
    telegram_handle = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    # Location & Education
    current_city_or_region = models.CharField(max_length=255, null=True, blank=True)
    current_education_level = models.CharField(max_length=255, null=True, blank=True)

    # Dynamic Selections
    course = models.ManyToManyField(Course, blank=True, related_name='registrations')
    intended_universities = models.ManyToManyField(University, blank=True)
    preferred_study_mode = models.ForeignKey(StudyMode, null=True, blank=True, on_delete=models.SET_NULL)
    ideal_class_times = models.ManyToManyField(ClassTimeOption, blank=True)

    # Goals and Financial Info
    top_goal = models.TextField(null=True, blank=True)
    apply_for_merit_discount = models.BooleanField(default=False)
    heard_about_us = models.CharField(max_length=255, null=True, blank=True)
    wants_premium = models.BooleanField(default=False)

    # Optional
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'course_registration'
        verbose_name = "Course Registration"
        verbose_name_plural = "Course Registrations"
        ordering = ['-created_at']
