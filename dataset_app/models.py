from django.db import models

class School(models.Model):
    school_id = models.AutoField(primary_key=True)  # AutoField for unique IDs
    school_name = models.CharField(max_length=100)

    def __str__(self):
        return self.school_name

class ClassRoom(models.Model):
    class_id = models.AutoField(primary_key=True)  # AutoField for unique IDs
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name

class Assignment(models.Model):
    assignment_id = models.AutoField(primary_key=True)  # AutoField for unique IDs
    assignment_name = models.CharField(max_length=100)

    def __str__(self):
        return self.assignment_name

class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)  # AutoField for unique IDs
    subject_name = models.CharField(max_length=100)
    subject_score = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)  # AutoField for unique IDs
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name='students')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='students')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='students')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    year = models.IntegerField()
    level = models.IntegerField()
    class_name = models.CharField(max_length=50)
    answers = models.CharField(max_length=5)
    correct_answers = models.CharField(max_length=5)
    question = models.IntegerField()
    subject_class = models.CharField(max_length=50)
    assessment = models.CharField(max_length=50)
    sydney_cc = models.FloatField()
    sydney_as = models.FloatField()
    sydney_ps = models.FloatField()
    student_s = models.FloatField()
    student_t = models.FloatField()
    student_a = models.FloatField()
    total_area = models.FloatField()
    participation = models.FloatField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"

class ExStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='ex_students')  # ForeignKey for relation
    student_name = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name

class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)  # AutoField for unique IDs
    answer_text = models.CharField(max_length=100)  # Renamed field for clarity

    def __str__(self):
        return self.answer_text

class Award(models.Model):
    award_id = models.AutoField(primary_key=True)  # AutoField for unique IDs
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
