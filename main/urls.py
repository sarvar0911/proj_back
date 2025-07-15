from django.urls import path
from .views import (
    CourseListView,
    UniversityListView,
    StudyModeListView,
    ClassTimeOptionListView,
    CourseRegistrationCreateView,
    CourseRegistrationListView,
)

urlpatterns = [
    path('courses/', CourseListView.as_view()),
    path('universities/', UniversityListView.as_view()),
    path('study-modes/', StudyModeListView.as_view()),
    path('class-times/', ClassTimeOptionListView.as_view()),
    path('register/', CourseRegistrationCreateView.as_view()),
    path('registrations/', CourseRegistrationListView.as_view()),
]
