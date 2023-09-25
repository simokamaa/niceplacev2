from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin


# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    
class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    previous_school = models.CharField(max_length=200)
    teaching_subjects = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now = True)
    role = models.CharField(max_length =200)
    
    def __str__(self):
        return self.first_name

class Staff(models.Model):
    profile_picture = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    start_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    
class School_blocks(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name
    
class class_block(models.Model):
    class_name = models.CharField(max_length=255, null=True, blank=True)
    school_block = models.ForeignKey(School_blocks, on_delete=models.CASCADE)
    class_teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    start_date = models.DateField(auto_now=True)
    
class Student(models.Model):
    admission_number = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    school_block = models.ForeignKey(School_blocks, on_delete=models.CASCADE)
    class_name = models.ForeignKey(class_block, on_delete=models.CASCADE)
    date_of_birth = models.DateTimeField(max_length=200)
    prevoius_school = models.CharField(max_length=200)
    guardian_first_name = models.CharField(max_length=200)
    guardian_middle_name = models.CharField(max_length=200)
    guardian_last_name = models.CharField(max_length=200)
    guardian_phone_number = models.CharField(max_length=200)
    guardian_relationship = models.CharField(max_length=200)
    date_of_admission = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name
        
    
class class_create(models.Model):
    class_name = models.CharField(max_length=255)
    class_teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    school_block = models.ForeignKey(class_block, on_delete = models.CASCADE)
    start_date = models.DateField(auto_now_add=True, null=True, blank=True)

class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    due_date = models.DateField()
    paid = models.BooleanField(default=False)
    payment_date = models.DateField(null=True, blank=True)
    payment_method = models.CharField(max_length=200,blank=True, null=True)
       

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    
class Notice(models.Model):
    notice = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add = True)
    author = models.CharField(max_length=255)
    
class Subject(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Exam(models.Model):
    name = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    block = models.ForeignKey(School_blocks, on_delete=models.CASCADE, blank=True, null=True)
    class_name = models.ForeignKey(class_block, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now = True, blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    
    
class ExamResult(models.Model):
    exam = models.ForeignKey(Exam, on_delete = models.CASCADE, blank=True, null=True)
    student = models.ForeignKey(Student, on_delete = models.CASCADE, blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE, blank=True, null=True)
    marks_obtained = models.DecimalField(max_digits = 5, decimal_places=2)
    grade = models.CharField(max_length=2)


    
class Assignment(models.Model):
    name = models.CharField(max_length=255)
    class_name = models.ForeignKey(class_block, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    due_date = models.DateField()
    description = models.TextField()
    
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete = models.CASCADE)
    score = models.DecimalField(max_digits = 5, decimal_places = 2)
    comment = models.TextField()
    graded_by = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    graded_at = models.DateTimeField(auto_now_add=True)
    

    