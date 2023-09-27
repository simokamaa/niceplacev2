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
    profile_picture = models.ImageField(upload_to="upload/", default="a.png", null=True, blank=True)
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
    prevoius_grade = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to="upload/", default="a.png")
    guardian_first_name = models.CharField(max_length=200)
    guardian_middle_name = models.CharField(max_length=200)
    guardian_last_name = models.CharField(max_length=200)
    guardian_phone_number = models.CharField(max_length=200)
    guardian_profile_picture = models.ImageField(upload_to="upload/", default='a.png')
    guardian_alternative_mobile_number = models.CharField(max_length=200)
    guardian_relationship = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField(null=True, blank=True, default=True)
    
    
    
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
    
    
class LibraryCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
class LibraryItem(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length = 20)
    publication_date = models.DateField(auto_now=True)
    category = models.ForeignKey(LibraryCategory, on_delete = models.CASCADE)
    
class LibraryItemCopy(models.Model):
    item = models.ForeignKey(LibraryItem, on_delete = models.CASCADE)
    copy_number = models.CharField(max_length=20)
    status = models.CharField(max_length=1, choices = [('A', 'Available'), ('L', 'Loaned'), ('R','Researved')])
    last_loan_date = models.DateTimeField(auto_now = True)
    last_borrower = models.ForeignKey(Student, on_delete = models.CASCADE)
    
class LibraryReservation(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    item_copy = models.ForeignKey(LibraryItemCopy, on_delete = models.CASCADE)
    date_reserved = models.DateField()
    status = models.CharField(max_length=1, choices = [('P', 'Pending'), ('C', 'Cancelled'), ('A', 'Approved')])
    
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
    
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=1, choices = [('P', 'Present'), ('A', 'Absent')])
    

    
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
    

    
class TransportationRoute(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    stops = models.ManyToManyField('TransportationStop', through = 'TransportationStopOrder')
    
class TransportationStop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
class TransportationStopOrder(models.Model):
    route = models.ForeignKey(TransportationRoute, on_delete = models.CASCADE)
    stop = models.ForeignKey(TransportationStop, on_delete = models.CASCADE)
    order = models.PositiveIntegerField()
    
class TransportationRequest(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    route = models.ForeignKey(TransportationRoute, on_delete = models.CASCADE)
    date_requested = models.DateField()
    status = models.CharField(max_length=1, choices = [('P', 'Pending'), ('A', 'Approved'),('R', 'Rejected')])
    approved_at = models.DateTimeField(null=True, blank=True)
    rejected_at = models.DateTimeField(null=True, blank=True)
    
class Opportunities(models.Model):
    title = models.CharField(max_length=255)
    subject_combination = models.CharField(max_length=255)
    School = models.CharField(max_length=255)
    posted_by = models.CharField(max_length=255)
    contact = models.IntegerField()
    Date_posted = models.DateField(auto_now_add = True)
    
    
class ELearning(models.Model):
    title = models.CharField(max_length=255)
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    link = models.SlugField()
    
class Message(models.Model):
    subject_combinations = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    status = models.BooleanField()
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.CharField(max_length=255)
    
class TimeTable(models.Model):
    DAY_CHOICES = (
        ('monday', 'monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Surtday', 'Surtday'),
        ('Sunday', 'Sunday')
    )
    block = models.ForeignKey(School_blocks, on_delete=models.CASCADE, null=True, blank=True)
    class_name = models.ForeignKey(class_block, on_delete=models.CASCADE, null=True, blank=True)
    Teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    day = models.CharField(max_length=255, choices = DAY_CHOICES, null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    activity = models.CharField(max_length=255, null=True, blank=True)
    date_produced = models.DateField(auto_now = True, null=True, blank=True)