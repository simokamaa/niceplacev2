from django.urls import path
from . import views , teacher_views, staff_views, student_views, subject_views, fee_views
from . import  exam_views, grade_views
from . import  Event_views, School_blocks_views, class_block_views
from . import  ExamResult_views

urlpatterns = [
    path('', views.index, name='index'),
    
    # urls for teacher view
    path('teacher_create/', teacher_views.teacher_create, name='teacher_create'),
    path('teachers_detail/', teacher_views.teachers_detail, name='teachers_detail'),
    path('teacher_detail/<int:pk>/', teacher_views.teacher_detail, name='teacher_detail'),
    path('teacher_update/<int:pk>/', teacher_views.teacher_update, name='teacher_update'),
    path('teacher_delete/<int:pk>/', teacher_views.teacher_delete, name='teacher_delete'),
    path('teachers_delete/', teacher_views.teachers_delete, name='teachers_delete'),
    
    # urls for staffs view
    path('staff_create/', staff_views.staff_create, name='staff_create'),
    path('staffs_detail/', staff_views.staffs_detail, name='staffs_detail'),
    path('staff_detail/<int:pk>/', staff_views.staff_detail, name='staff_detail'),
    path('staff_update/<int:pk>/', staff_views.staff_update, name='staff_update'),
    path('staff_delete/<int:pk>/', staff_views.staff_delete, name='staff_delete'),
    path('staffs_delete/', staff_views.staffs_delete, name='staffs_delete'),
    
    # urls for students view
    path('student_create/', student_views.student_create, name='student_create'),
    path('students_detail/', student_views.students_detail, name='students_detail'),
    path('student_detail/<int:pk>/', student_views.student_detail, name='student_detail'),
    path('student_update/<int:pk>/', student_views.student_update, name='student_update'),
    path('student_delete/<int:pk>/', student_views.student_delete, name='student_delete'),
    path('students_delete/', student_views.students_delete, name='students_delete'),
    
    # urls for subjects view
    path('subject_create/', subject_views.subject_create, name='subject_create'),
    path('subjects_detail/', subject_views.subjects_detail, name='subjects_detail'),
    path('subject_detail/<int:pk>/', subject_views.subject_detail, name='subject_detail'),
    path('subject_update/<int:pk>/', subject_views.subject_update, name='subject_update'),
    path('subject_delete/<int:pk>/', subject_views.subject_delete, name='subject_delete'),
    path('subjects_delete/', subject_views.subjects_delete, name='subjects_delete'),
    
    # urls for exams view
    path('exam_create/', exam_views.exam_create, name='exam_create'),
    path('exams_detail/', exam_views.exams_detail, name='exams_detail'),
    path('exam_detail/<int:pk>/', exam_views.exam_detail, name='exam_detail'),
    path('exam_update/<int:pk>/', exam_views.exam_update, name='exam_update'),
    path('exam_delete/<int:pk>/', exam_views.exam_delete, name='exam_delete'),
    path('exams_delete/', exam_views.exams_delete, name='exams_delete'),
    
    
    # urls for grades view
    path('grade_create/', grade_views.grade_create, name='grade_create'),
    path('grades_detail/', grade_views.grades_detail, name='grades_detail'),
    path('grade_detail/<int:pk>/', grade_views.grade_detail, name='grade_detail'),
    path('grade_update/<int:pk>/', grade_views.grade_update, name='grade_update'),
    path('grade_delete/<int:pk>/', grade_views.grade_delete, name='grade_delete'),
    path('grades_delete/', grade_views.grades_delete, name='grades_delete'),

 
    
    # urls for Event view
    path('Event_create/', Event_views.Event_create, name='Event_create'),
    path('Events_detail/', Event_views.Events_detail, name='Events_detail'),
    path('Event_detail/<int:pk>/', Event_views.Event_detail, name='Event_detail'),
    path('Event_update/<int:pk>/', Event_views.Event_update, name='Event_update'),
    path('Event_delete/<int:pk>/', Event_views.Event_delete, name='Event_delete'),
    path('Events_delete/', Event_views.Events_delete, name='Events_delete'),
    
    
    # urls for Event view
    path('School_blocks_create/', School_blocks_views.School_blocks_create, name='School_blocks_create'),
    path('School_blockss_detail/', School_blocks_views.School_blockss_detail, name='School_blockss_detail'),
    path('School_blocks_detail/<int:pk>/', School_blocks_views.School_blocks_detail, name='School_blocks_detail'),
    path('School_blocks_update/<int:pk>/', School_blocks_views.School_blocks_update, name='School_blocks_update'),
    path('School_blocks_delete/<int:pk>/', School_blocks_views.School_blocks_delete, name='School_blocks_delete'),
    path('School_blockss_delete/', School_blocks_views.School_blockss_delete, name='School_blockss_delete'),
    
    # urls for Event view
    path('class_block_create/', class_block_views.class_block_create, name='class_block_create'),
    path('class_blocks_detail/', class_block_views.class_blocks_detail, name='class_blocks_detail'),
    path('class_block_detail/<int:pk>/', class_block_views.class_block_detail, name='class_block_detail'),
    path('class_block_update/<int:pk>/', class_block_views.class_block_update, name='class_block_update'),
    path('class_block_delete/<int:pk>/', class_block_views.class_block_delete, name='class_block_delete'),
    path('class_blocks_delete/', class_block_views.class_blocks_delete, name='class_blocks_delete'),
        
    # urls for ExamResult view
    path('ExamResult_create/', ExamResult_views.ExamResult_create, name='ExamResult_create'),
    path('ExamResults_detail/', ExamResult_views.ExamResults_detail, name='ExamResults_detail'),
    path('ExamResult_detail/<int:pk>/', ExamResult_views.ExamResult_detail, name='ExamResult_detail'),
    path('ExamResult_update/<int:pk>/', ExamResult_views.ExamResult_update, name='ExamResult_update'),
    path('ExamResult_delete/<int:pk>/', ExamResult_views.ExamResult_delete, name='ExamResult_delete'),
    path('ExamResults_delete/', ExamResult_views.ExamResults_delete, name='ExamResults_delete'),
]
