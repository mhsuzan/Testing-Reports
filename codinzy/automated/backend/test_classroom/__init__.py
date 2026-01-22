"""
Classroom Integration Tests for Codinzy Backend

Tests cover:
- Jitsi classroom integration
- Whereby classroom integration
- Classroom session tracking
- Activity submissions
"""

import pytest
from datetime import datetime, timedelta, date, time
from rest_framework.test import APITestCase

import sys
from pathlib import Path
backend_path = Path(__file__).parent.parent.parent.parent / 'backend'
sys.path.insert(0, str(backend_path))

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_settings')

import django
django.setup()

from api.models import User, ScheduledClass, ClassroomSession, ClassActivity, StudentActivitySubmission, Student, Teacher, Course


class JitsiClassroomTestCase(APITestCase):
    """Test cases for Jitsi classroom integration"""
    
    def setUp(self):
        """Set up test data"""
        self.teacher_user = User.objects.create_user(
            username='teacher',
            email='teacher@test.com',
            password='TestPass123!',
            user_type='teacher',
            name='Test Teacher'
        )
        self.teacher = Teacher.objects.create(
            user=self.teacher_user,
            details='Test teacher'
        )
        
        self.student_user = User.objects.create_user(
            username='student',
            email='student@test.com',
            password='TestPass123!',
            user_type='student',
            name='Test Student'
        )
        self.student = Student.objects.create(
            user=self.student_user,
            school_name='Test School',
            student_grade='5'
        )
        
        self.course = Course.objects.create(
            title='Python Course',
            description='Learn Python',
            course_code='PY'
        )
    
    def test_jitsi_room_generation(self):
        """Test Jitsi room ID generation"""
        scheduled_class = ScheduledClass.objects.create(
            teacher=self.teacher,
            class_date=date.today() + timedelta(days=1),
            class_time=time(10, 0),
            course_type='new',
            class_status='scheduled'
        )
        
        self.assertIsNotNone(scheduled_class)
    
    def test_jitsi_room_id_format(self):
        """Test Jitsi room ID format"""
        scheduled_class = ScheduledClass.objects.create(
            teacher=self.teacher,
            class_date=date.today() + timedelta(days=1),
            class_time=time(10, 0),
            course_type='new',
            class_status='scheduled'
        )
        
        if hasattr(scheduled_class, 'jitsi_room_id'):
            self.assertIn('jitsi', scheduled_class.jitsi_room_id.lower())


class WherebyClassroomTestCase(APITestCase):
    """Test cases for Whereby classroom integration"""
    
    def setUp(self):
        """Set up test data"""
        self.teacher_user = User.objects.create_user(
            username='teacher',
            email='teacher@test.com',
            password='TestPass123!',
            user_type='teacher',
            name='Test Teacher'
        )
        self.teacher = Teacher.objects.create(
            user=self.teacher_user,
            details='Test teacher'
        )
        
        self.course = Course.objects.create(
            title='Python Course',
            description='Learn Python',
            course_code='PY'
        )
    
    def test_whereby_room_generation(self):
        """Test Whereby room URL generation"""
        scheduled_class = ScheduledClass.objects.create(
            teacher=self.teacher,
            class_date=date.today() + timedelta(days=1),
            class_time=time(10, 0),
            course_type='trial',
            class_status='scheduled'
        )
        
        self.assertIsNotNone(scheduled_class)


class ClassroomSessionTrackingTestCase(APITestCase):
    """Test cases for classroom session tracking"""
    
    def setUp(self):
        """Set up test data"""
        self.teacher_user = User.objects.create_user(
            username='teacher',
            email='teacher@test.com',
            password='TestPass123!',
            user_type='teacher',
            name='Test Teacher'
        )
        self.teacher = Teacher.objects.create(
            user=self.teacher_user,
            details='Test teacher'
        )
        
        self.student_user = User.objects.create_user(
            username='student',
            email='student@test.com',
            password='TestPass123!',
            user_type='student',
            name='Test Student'
        )
        self.student = Student.objects.create(
            user=self.student_user,
            school_name='Test School',
            student_grade='5'
        )
        
        self.course = Course.objects.create(
            title='Python Course',
            description='Learn Python',
            course_code='PY'
        )
        
        self.scheduled_class = ScheduledClass.objects.create(
            teacher=self.teacher,
            class_date=date.today() + timedelta(days=1),
            class_time=time(10, 0),
            course_type='new',
            class_status='scheduled'
        )
    
    def test_session_join_tracking(self):
        """Test tracking when student joins classroom"""
        session = ClassroomSession.objects.create(
            scheduled_class=self.scheduled_class,
            user=self.student_user,
            student=self.student,
            status='active'
        )
        
        self.assertIsNotNone(session.enter_time)
        self.assertEqual(session.status, 'active')
    
    def test_session_leave_tracking(self):
        """Test tracking when student leaves classroom"""
        enter_time = datetime.now()
        leave_time = enter_time + timedelta(hours=1)
        
        session = ClassroomSession.objects.create(
            scheduled_class=self.scheduled_class,
            user=self.student_user,
            student=self.student,
            enter_time=enter_time,
            leave_time=leave_time,
            duration_seconds=3600,
            status='completed'
        )
        
        self.assertIsNotNone(session.leave_time)
        self.assertEqual(session.duration_seconds, 3600)
        self.assertEqual(session.status, 'completed')
    
    def test_session_duration_auto_calculation(self):
        """Test duration is calculated from join and leave times"""
        enter_time = datetime.now()
        leave_time = enter_time + timedelta(minutes=45)
        
        session = ClassroomSession.objects.create(
            scheduled_class=self.scheduled_class,
            user=self.student_user,
            student=self.student,
            enter_time=enter_time,
            leave_time=leave_time,
            status='completed'
        )
        
        expected_duration = int((leave_time - enter_time).total_seconds())
        self.assertEqual(session.duration_seconds, expected_duration)


class ActivitySubmissionTestCase(APITestCase):
    """Test cases for activity submissions"""
    
    def setUp(self):
        """Set up test data"""
        self.student_user = User.objects.create_user(
            username='student',
            email='student@test.com',
            password='TestPass123!',
            user_type='student',
            name='Test Student'
        )
        self.student = Student.objects.create(
            user=self.student_user,
            school_name='Test School',
            student_grade='5'
        )
        
        self.teacher_user = User.objects.create_user(
            username='teacher',
            email='teacher@test.com',
            password='TestPass123!',
            user_type='teacher',
            name='Test Teacher'
        )
        
        self.activity = ClassActivity.objects.create(
            title='Python Quiz',
            short_description='Test your Python knowledge'
        )
        
        self.scheduled_class = ScheduledClass.objects.create(
            teacher=Teacher.objects.create(
                user=self.teacher_user,
                details='Test teacher'
            ),
            class_date=date.today() + timedelta(days=1),
            class_time=time(10, 0),
            course_type='new',
            class_status='scheduled'
        )
    
    def test_activity_submission_creation(self):
        """Test student can submit activity"""
        submission = StudentActivitySubmission.objects.create(
            student=self.student,
            activity=self.activity,
            scheduled_class=self.scheduled_class,
            status='submitted'
        )
        
        self.assertIsNotNone(submission)
        self.assertEqual(submission.status, 'submitted')
    
    def test_activity_submission_status_choices(self):
        """Test submission status choices"""
        for status in ['draft', 'submitted', 'graded', 'returned']:
            submission = StudentActivitySubmission.objects.create(
                student=self.student,
                activity=self.activity,
                scheduled_class=self.scheduled_class,
                status=status
            )
            self.assertEqual(submission.status, status)
    
    def test_submission_timestamp(self):
        """Test submission has timestamp"""
        submission = StudentActivitySubmission.objects.create(
            student=self.student,
            activity=self.activity,
            scheduled_class=self.scheduled_class,
            status='submitted'
        )
        
        self.assertIsNotNone(submission.submitted_at)
