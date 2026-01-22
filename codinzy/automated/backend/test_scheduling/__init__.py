"""
Scheduled Class Tests for Codinzy Backend

Tests cover:
- Class scheduling
- Class status transitions
- Teacher availability
- Rescheduling functionality
"""

import pytest
from datetime import datetime, timedelta, time, date
from rest_framework.test import APITestCase

import sys
from pathlib import Path
backend_path = Path(__file__).parent.parent.parent.parent / 'backend'
sys.path.insert(0, str(backend_path))

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_settings')

import django
django.setup()

from api.models import User, ScheduledClass, TeacherAvailability, ClassroomSession, Course, Teacher, Student


class ScheduledClassModelTestCase(APITestCase):
    """Test cases for ScheduledClass model"""
    
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
            details='Test teacher details'
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
    
    def test_scheduled_class_creation(self):
        """Test scheduled class creation"""
        scheduled_class = ScheduledClass.objects.create(
            class_date=date.today() + timedelta(days=1),
            class_time=time(10, 0),
            teacher=self.teacher,
            class_status='scheduled'
        )
        
        self.assertIsNotNone(scheduled_class)
        self.assertEqual(scheduled_class.class_status, 'scheduled')
    
    def test_scheduled_class_status_choices(self):
        """Test status field choices"""
        for status in ['scheduled', 'incomplete', 'complete']:
            scheduled_class = ScheduledClass.objects.create(
                class_date=date.today() + timedelta(days=1),
                class_time=time(10, 0),
                teacher=self.teacher,
                class_status=status
            )
            self.assertEqual(scheduled_class.class_status, status)
    
    def test_scheduled_class_type_choices(self):
        """Test course_type field choices"""
        for course_type in ['new', 'renewal', 'trial']:
            scheduled_class = ScheduledClass.objects.create(
                class_date=date.today() + timedelta(days=1),
                class_time=time(10, 0),
                teacher=self.teacher,
                course_type=course_type
            )
            self.assertEqual(scheduled_class.course_type, course_type)
    
    def test_scheduled_class_str_representation(self):
        """Test scheduled class string representation"""
        scheduled_class = ScheduledClass.objects.create(
            class_date=date.today() + timedelta(days=1),
            class_time=time(10, 0),
            teacher=self.teacher
        )
        
        self.assertIn('Unassigned Lesson', str(scheduled_class))
    
    def test_scheduled_class_students_relationship(self):
        """Test scheduled class can have multiple students"""
        scheduled_class = ScheduledClass.objects.create(
            class_date=date.today() + timedelta(days=1),
            class_time=time(10, 0),
            teacher=self.teacher
        )
        
        scheduled_class.students_attended.add(self.student)
        
        self.assertEqual(scheduled_class.students_attended.count(), 1)
        self.assertIn(self.student, scheduled_class.students_attended.all())
    
    def test_class_status_transition_scheduled_to_complete(self):
        """Test class status can transition from scheduled to complete"""
        scheduled_class = ScheduledClass.objects.create(
            class_date=date.today() + timedelta(days=1),
            class_time=time(10, 0),
            teacher=self.teacher,
            class_status='scheduled'
        )
        
        scheduled_class.class_status = 'complete'
        scheduled_class.save()
        
        self.assertEqual(scheduled_class.class_status, 'complete')
    
    def test_class_status_transition_scheduled_to_incomplete(self):
        """Test class status can transition from scheduled to incomplete"""
        scheduled_class = ScheduledClass.objects.create(
            class_date=date.today() + timedelta(days=1),
            class_time=time(10, 0),
            teacher=self.teacher,
            class_status='scheduled'
        )
        
        scheduled_class.class_status = 'incomplete'
        scheduled_class.save()
        
        self.assertEqual(scheduled_class.class_status, 'incomplete')


class TeacherAvailabilityTestCase(APITestCase):
    """Test cases for TeacherAvailability model"""
    
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
            details='Test teacher details'
        )
    
    def test_teacher_availability_creation(self):
        """Test teacher availability creation"""
        start_dt = datetime.now() + timedelta(days=1)
        end_dt = start_dt + timedelta(hours=8)
        
        availability = TeacherAvailability.objects.create(
            teacher=self.teacher,
            start_time=start_dt,
            end_time=end_dt
        )
        
        self.assertIsNotNone(availability)
        self.assertEqual(availability.teacher, self.teacher)
    
    def test_teacher_availability_str_representation(self):
        """Test teacher availability string representation"""
        start_dt = datetime.now() + timedelta(days=1)
        end_dt = start_dt + timedelta(hours=8)
        
        availability = TeacherAvailability.objects.create(
            teacher=self.teacher,
            start_time=start_dt,
            end_time=end_dt
        )
        
        self.assertIn('Test Teacher', str(availability))
    
    def test_multiple_availability_entries(self):
        """Test teacher can have multiple availability entries"""
        for i in range(3):
            start_dt = datetime.now() + timedelta(days=i+1)
            end_dt = start_dt + timedelta(hours=8)
            TeacherAvailability.objects.create(
                teacher=self.teacher,
                start_time=start_dt,
                end_time=end_dt
            )
        
        self.assertEqual(self.teacher.availabilities.count(), 3)


class ClassroomSessionTestCase(APITestCase):
    """Test cases for ClassroomSession model"""
    
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
            details='Test teacher details'
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
        
        self.scheduled_class = ScheduledClass.objects.create(
            class_date=date.today() + timedelta(days=1),
            class_time=time(10, 0),
            teacher=self.teacher,
            class_status='scheduled'
        )
    
    def test_classroom_session_creation(self):
        """Test classroom session creation"""
        session = ClassroomSession.objects.create(
            scheduled_class=self.scheduled_class,
            user=self.student_user,
            student=self.student,
            enter_time=datetime.now(),
            leave_time=datetime.now() + timedelta(hours=1),
            duration_seconds=3600,
            status='completed'
        )
        
        self.assertIsNotNone(session)
        self.assertEqual(session.duration_seconds, 3600)
        self.assertEqual(session.status, 'completed')
    
    def test_classroom_session_status_choices(self):
        """Test status field choices"""
        user1 = User.objects.create_user(
            username='session_user1', email='session1@test.com',
            password='TestPass123!', user_type='student'
        )
        user2 = User.objects.create_user(
            username='session_user2', email='session2@test.com',
            password='TestPass123!', user_type='student'
        )
        user3 = User.objects.create_user(
            username='session_user3', email='session3@test.com',
            password='TestPass123!', user_type='student'
        )
        
        session1 = ClassroomSession.objects.create(
            scheduled_class=self.scheduled_class,
            user=user1,
            status='active'
        )
        self.assertEqual(session1.status, 'active')
        
        session2 = ClassroomSession.objects.create(
            scheduled_class=self.scheduled_class,
            user=user2,
            status='completed'
        )
        self.assertEqual(session2.status, 'completed')
        
        session3 = ClassroomSession.objects.create(
            scheduled_class=self.scheduled_class,
            user=user3,
            status='abandoned'
        )
        self.assertEqual(session3.status, 'abandoned')
    
    def test_classroom_session_str_representation(self):
        """Test classroom session string representation"""
        session = ClassroomSession.objects.create(
            scheduled_class=self.scheduled_class,
            user=self.student_user,
            status='completed'
        )
        
        self.assertIn('Test Student', str(session))
    
    def test_classroom_session_duration_calculation(self):
        """Test duration calculation"""
        start = datetime.now()
        end = start + timedelta(hours=1, minutes=30)
        
        session = ClassroomSession.objects.create(
            scheduled_class=self.scheduled_class,
            user=self.student_user,
            enter_time=start,
            leave_time=end,
            status='completed'
        )
        
        self.assertEqual(session.duration_seconds, 5400)
