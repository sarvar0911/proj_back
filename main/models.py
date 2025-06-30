from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'course'
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class CourseRegistration(models.Model):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_name} | {self.course.name}'

    class Meta:
        db_table = 'course_registration'
        verbose_name = "Course Registration"
        verbose_name_plural = "Course Registrations"
