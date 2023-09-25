from django.forms import ModelForm
from . models import *

class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'
        
class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
        
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        
class School_blocksForm(ModelForm):
    class Meta:
        model = School_blocks
        fields = '__all__'
        
class Class_blockForm(ModelForm):
    class Meta:
        model = class_block
        fields = '__all__'
        
class FeeForm(ModelForm):
    class Meta:
        model = Fee
        fields = '__all__'
        
        
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        
class NoticeForm(ModelForm):
    class Meta:
        model = Notice
        fields = '__all__'
        
        
class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
        
class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'
        
class ExamResultForm(ModelForm):
    class Meta:
        model = ExamResult
        fields = '__all__'
        
        
class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'
        
class GradeForm(ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'
        
  
