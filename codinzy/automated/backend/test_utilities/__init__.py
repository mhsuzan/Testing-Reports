"""
Utilities Tests for Codinzy Backend

Tests cover:
- Audit logging
- UTM tracking utilities
- Date/time utilities
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

from api.models import User, Student, Course


class UserTimezoneTestCase(APITestCase):
    """Test cases for user timezone handling"""
    
    def test_user_timezone_default(self):
        """Test user timezone defaults to UTC"""
        user = User.objects.create_user(
            username='student',
            email='student@test.com',
            password='TestPass123!',
            user_type='student'
        )
        
        self.assertEqual(user.timezone, 'UTC')
    
    def test_user_timezone_custom(self):
        """Test user can have custom timezone"""
        user = User.objects.create_user(
            username='student',
            email='student@test.com',
            password='TestPass123!',
            user_type='student',
            timezone='America/New_York'
        )
        
        self.assertEqual(user.timezone, 'America/New_York')


class AuditFieldsTestCase(APITestCase):
    """Test cases for audit fields"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='teacher',
            email='teacher@test.com',
            password='TestPass123!',
            user_type='teacher',
            name='Test Teacher'
        )
    
    def test_course_created_by(self):
        """Test course created_by field"""
        course = Course.objects.create(
            title='Python Course',
            description='Learn Python',
            course_code='PY',
            created_by=self.user
        )
        
        self.assertEqual(course.created_by, self.user)
    
    def test_course_timestamp_fields(self):
        """Test course has timestamp fields"""
        course = Course.objects.create(
            title='Python Course',
            description='Learn Python',
            course_code='PY'
        )
        
        self.assertIsNotNone(course.created_at)
        self.assertIsNotNone(course.last_updated_at)


class UserPreferencesTestCase(APITestCase):
    """Test cases for user preferences"""
    
    def test_user_language_spokes_default(self):
        """Test language spokes defaults to empty list"""
        user = User.objects.create_user(
            username='student',
            email='student@test.com',
            password='TestPass123!',
            user_type='student'
        )
        
        self.assertEqual(user.language_spokes, [])
    
    def test_user_language_spokes_custom(self):
        """Test user can have custom language spokes"""
        user = User.objects.create_user(
            username='student',
            email='student@test.com',
            password='TestPass123!',
            user_type='student',
            language_spokes=['English', 'Spanish', 'French']
        )
        
        self.assertEqual(user.language_spokes, ['English', 'Spanish', 'French'])
    
    def test_user_country_field(self):
        """Test user can have country"""
        user = User.objects.create_user(
            username='student',
            email='student@test.com',
            password='TestPass123!',
            user_type='student',
            country='US'
        )
        
        self.assertEqual(user.country, 'US')
    
    def test_user_phone_number(self):
        """Test user can have phone number"""
        user = User.objects.create_user(
            username='student',
            email='student@test.com',
            password='TestPass123!',
            user_type='student',
            phone_number='+1234567890'
        )
        
        self.assertEqual(user.phone_number, '+1234567890')


class UserPermissionsTestCase(APITestCase):
    """Test cases for user permissions"""
    
    def test_user_is_lm_default(self):
        """Test is_lm defaults to False"""
        user = User.objects.create_user(
            username='student',
            email='student@test.com',
            password='TestPass123!',
            user_type='student'
        )
        
        self.assertFalse(user.is_lm)
    
    def test_user_redash_access_default(self):
        """Test redash_access defaults to False"""
        user = User.objects.create_user(
            username='student',
            email='student@test.com',
            password='TestPass123!',
            user_type='student'
        )
        
        self.assertFalse(user.redash_access)
    
    def test_admin_has_permissions(self):
        """Test admin user has staff permissions"""
        admin = User.objects.create_user(
            username='admin',
            email='admin@test.com',
            password='TestPass123!',
            user_type='admin',
            is_staff=True
        )
        
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_admin())
