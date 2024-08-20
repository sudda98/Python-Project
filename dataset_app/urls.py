


from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.student_list, name='home'), 
#     path('students/', views.student_list, name='student_list'),
#     path('csv-data/', views.csv_view, name='csv_view'),
# ]




urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('schools/', views.school_list, name='school_list'),
    path('classrooms/', views.classroom_list, name='classroom_list'),
    path('assignments/', views.assignment_list, name='assignment_list'),
    path('exstudents/', views.exstudent_list, name='exstudent_list'),
    path('answers/', views.answer_list, name='answer_list'),
    path('awards/', views.award_list, name='award_list'),
    path('subjects/', views.subject_list, name='subject_list'),
]
