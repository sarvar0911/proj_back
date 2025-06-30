from django.urls import path

from main import views

urlpatterns = [
    path('courses/', views.CourseListView.as_view(), name='courses'),
    path('registrations/', views.CourseRegistrationListView.as_view()),
    path('register/', views.CourseRegistrationCreateView.as_view()),
]