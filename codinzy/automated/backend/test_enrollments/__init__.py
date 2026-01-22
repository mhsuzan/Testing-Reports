"""
Enrollment Tests for Codinzy Backend

Tests cover:
- Enrollment creation and management
- Enrollment status tracking
- Enrollment progress
"""

import pytest
from datetime import datetime, timedelta
from rest_framework.test import APITestCase

import sys
from pathlib import Path
backend_path = Path(__file__).parent.parent.parent.parent / 'backend'
sys.path.insert(0, str(backend_path))

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_settings')

import django
django.setup()

from api.models import User, Enrollment, Student, Course, Payment


class EnrollmentModelTestCase(APITestCase):
    """Test cases for Enrollment model"""
    
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
        
        self.course = Course.objects.create(
            title='Python Course',
            description='Learn Python',
            course_code='PY'
        )
    
    def test_enrollment_creation(self):
        """Test enrollment creation"""
        enrollment = Enrollment.objects.create(
            student=self.student,
            course='Python Course'
        )
        
        self.assertIsNotNone(enrollment)
        self.assertEqual(enrollment.student, self.student)
        self.assertEqual(enrollment.course, 'Python Course')
    
    def test_enrollment_str_representation(self):
        """Test enrollment string representation"""
        enrollment = Enrollment.objects.create(
            student=self.student,
            course='Python Course'
        )
        
        self.assertIn('Test Student', str(enrollment))


class EnrollmentProgressTestCase(APITestCase):
    """Test cases for enrollment progress tracking"""
    
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
    
    def test_enrollment_with_service_type(self):
        """Test enrollment with service type"""
        enrollment = Enrollment.objects.create(
            student=self.student,
            course='Python Course',
            service_type='Prime'
        )
        
        self.assertEqual(enrollment.service_type, 'Prime')
