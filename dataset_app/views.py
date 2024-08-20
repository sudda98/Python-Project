# from django.shortcuts import render
# from dataset_app.models import Student
import pandas as pd
import os
from django.conf import settings


from django.shortcuts import render, get_object_or_404
from .models import Student, School, ClassRoom, Assignment, ExStudent, Answer, Award, Subject



def student_list(request):
    students = Student.objects.all()
    return render(request, 'dataset_app/student_list.html', {'students': students})


def student_list(request):
    School = School.objects.all()
    return render(request, 'dataset_app/school_list.html', {'School': School})



def csv_view(request):
    # Use Django's settings for media files
    csv_path = os.path.join(settings.MEDIA_ROOT, 'ganison_datasets/ganison_dataset_6.csv')
    
    try:
        # Read the CSV file
        df = pd.read_csv(csv_path)
        # Convert DataFrame to HTML table
        html_table = df.to_html()
    except FileNotFoundError:
        html_table = '<p>File not found.</p>'
    except Exception as e:
        html_table = f'<p>An error occurred: {e}</p>'

    return render(request, 'dataset_app/csv_view.html', {'table': html_table})



def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    return render(request, 'students/student_detail.html', {'student': student})

def school_list(request):
    schools = School.objects.all()
    return render(request, 'schools/school_list.html', {'schools': schools})

def classroom_list(request):
    classrooms = ClassRoom.objects.all()
    return render(request, 'classrooms/classroom_list.html', {'classrooms': classrooms})

def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'assignments/assignment_list.html', {'assignments': assignments})

def exstudent_list(request):
    exstudents = ExStudent.objects.all()
    return render(request, 'exstudents/exstudent_list.html', {'exstudents': exstudents})

def answer_list(request):
    answers = Answer.objects.all()
    return render(request, 'answers/answer_list.html', {'answers': answers})

def award_list(request):
    awards = Award.objects.all()
    return render(request, 'awards/award_list.html', {'awards': awards})

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects/subject_list.html', {'subjects': subjects})
