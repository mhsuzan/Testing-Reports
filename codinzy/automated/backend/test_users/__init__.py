"""
User Model Tests for Codinzy Backend

Tests cover:
- User model validation
- Teacher profile operations
- Student profile operations
- User profile management
"""

import pytest
from django.core.exceptions import ValidationError
from rest_framework.test import APITestCase
from django.db import IntegrityError

import sys
from pathlib import Path
backend_path = Path(__file__).parent.parent.parent.parent / 'backend'
sys.path.insert(0, str(backend_path))

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_settings')

import django
django.setup()

from api.models import User, Student, Teacher


class UserModelTestCase(APITestCase):
    """Test cases for User model"""
    
    def test_user_creation_minimal(self):
        """Test user creation with minimal data"""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123!'
        )
        
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('TestPass123!'))
    
    def test_user_creation_with_name(self):
        """Test user creation with name"""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123!',
            name='Test User'
        )
        
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.get_full_name(), 'Test User')
    
    def test_user_type_default(self):
        """Test user type defaults to 'student'"""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123!'
        )
        
        self.assertEqual(user.user_type, 'student')
    
    def test_user_type_choice_student(self):
        """Test user with student type"""
        user = User.objects.create_user(
            username='student',
            email='student@test.com',
            password='TestPass123!',
            user_type='student'
        )
        
        self.assertTrue(user.is_student())
        self.assertFalse(user.is_teacher())
        self.assertFalse(user.is_admin())
    
    def test_user_type_choice_teacher(self):
        """Test user with teacher type"""
        user = User.objects.create_user(
            username='teacher',
            email='teacher@test.com',
            password='TestPass123!',
            user_type='teacher'
        )
        
        self.assertTrue(user.is_teacher())
        self.assertFalse(user.is_student())
        self.assertFalse(user.is_admin())
    
    def test_user_type_choice_admin(self):
        """Test user with admin type"""
        user = User.objects.create_user(
            username='admin',
            email='admin@test.com',
            password='TestPass123!',
            user_type='admin'
        )
        
        self.assertTrue(user.is_admin())
        self.assertFalse(user.is_student())
        self.assertFalse(user.is_teacher())
    
    def test_superuser_is_admin(self):
        """Test superuser is considered admin"""
        user = User.objects.create_superuser(
            username='superuser',
            email='super@test.com',
            password='TestPass123!'
        )
        
        self.assertTrue(user.is_admin())
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
    
    def test_username_uniqueness(self):
        """Test username must be unique"""
        User.objects.create_user(
            username='testuser',
            email='test1@example.com',
            password='TestPass123!'
        )
        
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                username='testuser',
                email='test2@example.com',
                password='TestPass123!'
            )
    
    def test_email_uniqueness(self):
        """Test email must be unique"""
        User.objects.create_user(
            username='user1',
            email='test@example.com',
            password='TestPass123!'
        )
        
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                username='user2',
                email='test@example.com',
                password='TestPass123!'
            )
    
    def test_referral_code_generation(self):
        """Test referral code is auto-generated on save"""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123!'
        )
        
        self.assertIsNotNone(user.referral_code)
        self.assertEqual(len(user.referral_code), 5)
        self.assertTrue(user.referral_code.isalnum())
    
    def test_referral_code_unique(self):
        """Test referral codes are unique"""
        user1 = User.objects.create_user(
            username='user1',
            email='user1@example.com',
            password='TestPass123!'
        )
        user2 = User.objects.create_user(
            username='user2',
            email='user2@example.com',
            password='TestPass123!'
        )
        
        self.assertNotEqual(user1.referral_code, user2.referral_code)
    
    def test_timezone_default(self):
        """Test timezone defaults to UTC"""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123!'
        )
        
        self.assertEqual(user.timezone, 'UTC')
    
    def test_language_spokes_default(self):
        """Test language spokes defaults to empty list"""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123!'
        )
        
        self.assertEqual(user.language_spokes, [])
    
    def test_profile_picture_upload(self):
        """Test profile picture field exists"""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123!'
        )
        
        self.assertTrue(hasattr(user, 'profile_picture'))
    
    def test_phone_number_field(self):
        """Test phone number field exists"""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123!',
            phone_number='+1234567890'
        )
        
        self.assertEqual(user.phone_number, '+1234567890')
    
    def test_country_field(self):
        """Test country field exists"""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123!',
            country='US'
        )
        
        self.assertEqual(user.country, 'US')
    
    def test_gender_field(self):
        """Test gender field exists"""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123!',
            gender='M'
        )
        
        self.assertEqual(user.gender, 'M')
    
    def test_is_lm_field(self):
        """Test is_lm field defaults to False"""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123!'
        )
        
        self.assertFalse(user.is_lm)
    
    def test_redash_access_field(self):
        """Test redash_access field defaults to False"""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123!'
        )
        
        self.assertFalse(user.redash_access)
    
    def test_utm_tracking_field(self):
        """Test utm_tracking field exists"""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123!'
        )
        
        self.assertTrue(hasattr(user, 'utm_tracking'))
        self.assertIsNone(user.utm_tracking)


class TeacherModelTestCase(APITestCase):
    """Test cases for Teacher model"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='teacher',
            email='teacher@test.com',
            password='TestPass123!',
            user_type='teacher',
            name='Test Teacher'
        )
    
    def test_teacher_creation(self):
        """Test teacher creation"""
        teacher = Teacher.objects.create(
            user=self.user,
            details='Test teacher details',
            qualification='Masters',
            experience_years='5'
        )
        
        self.assertIsNotNone(teacher)
        self.assertEqual(teacher.user, self.user)
        self.assertEqual(teacher.details, 'Test teacher details')
    
    def test_teacher_name_property(self):
        """Test teacher name property returns user name"""
        teacher = Teacher.objects.create(
            user=self.user,
            details='Test details'
        )
        
        self.assertEqual(teacher.name, 'Test Teacher')
    
    def test_teacher_email_property(self):
        """Test teacher email property returns user email"""
        teacher = Teacher.objects.create(
            user=self.user,
            details='Test details'
        )
        
        self.assertEqual(teacher.email, 'teacher@test.com')
    
    def test_teacher_str_representation(self):
        """Test teacher string representation"""
        teacher = Teacher.objects.create(
            user=self.user,
            details='Test details'
        )
        
        self.assertEqual(str(teacher), 'Test Teacher')
    
    def test_teacher_without_user(self):
        """Test teacher can exist without user"""
        teacher = Teacher.objects.create(
            details='Independent teacher'
        )
        
        self.assertIsNone(teacher.user)
        self.assertIn('Teacher', str(teacher))
    
    def test_teacher_kyt_upload(self):
        """Test KYT document field"""
        teacher = Teacher.objects.create(
            user=self.user,
            details='Test details'
        )
        
        self.assertTrue(hasattr(teacher, 'kyt'))
        self.assertIsNone(teacher.kyt)
    
    def test_teacher_signature_upload(self):
        """Test signature field"""
        teacher = Teacher.objects.create(
            user=self.user,
            details='Test details'
        )
        
        self.assertTrue(hasattr(teacher, 'signature'))
        self.assertIsNone(teacher.signature)
    
    def test_teacher_week_off_default(self):
        """Test week off defaults to empty list"""
        teacher = Teacher.objects.create(
            user=self.user,
            details='Test details'
        )
        
        self.assertEqual(teacher.week_off, [])
    
    def test_teacher_account_active_default(self):
        """Test account_active defaults to 'unverified'"""
        teacher = Teacher.objects.create(
            user=self.user,
            details='Test details'
        )
        
        self.assertEqual(teacher.account_active, 'unverified')
    
    def test_teacher_account_active_choices(self):
        """Test account_active field choices"""
        for status in ['active', 'unverified', 'inactive']:
            teacher = Teacher.objects.create(
                user=self.user,
                details='Test details',
                account_active=status
            )
            self.assertEqual(teacher.account_active, status)


class StudentModelTestCase(APITestCase):
    """Test cases for Student model"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='student',
            email='student@test.com',
            password='TestPass123!',
            user_type='student',
            name='Test Student'
        )
    
    def test_student_creation(self):
        """Test student creation"""
        student = Student.objects.create(
            user=self.user,
            school_name='Test School',
            student_grade='5'
        )
        
        self.assertIsNotNone(student)
        self.assertEqual(student.user, self.user)
        self.assertEqual(student.school_name, 'Test School')
        self.assertEqual(student.student_grade, '5')
    
    def test_student_name_property(self):
        """Test student name property returns user name"""
        student = Student.objects.create(
            user=self.user,
            school_name='Test School',
            student_grade='5'
        )
        
        self.assertEqual(student.name, 'Test Student')
    
    def test_student_email_property(self):
        """Test student email property returns user email"""
        student = Student.objects.create(
            user=self.user,
            school_name='Test School',
            student_grade='5'
        )
        
        self.assertEqual(student.email, 'student@test.com')
    
    def test_student_phone_property(self):
        """Test student phone property returns user phone"""
        self.user.phone_number = '+1234567890'
        self.user.save()
        
        student = Student.objects.create(
            user=self.user,
            school_name='Test School',
            student_grade='5'
        )
        
        self.assertEqual(student.phone_number, '+1234567890')
    
    def test_student_str_representation(self):
        """Test student string representation"""
        student = Student.objects.create(
            user=self.user,
            school_name='Test School',
            student_grade='5'
        )
        
        self.assertEqual(str(student), 'Test Student')
    
    def test_student_without_user(self):
        """Test student can exist without user"""
        student = Student.objects.create(
            school_name='Independent School',
            student_grade='6'
        )
        
        self.assertIsNone(student.user)
        self.assertIn('Student', str(student))
    
    def test_student_grade_choices(self):
        """Test student grade field choices"""
        for grade in range(1, 13):
            student = Student.objects.create(
                school_name='Test School',
                student_grade=str(grade)
            )
            self.assertEqual(student.student_grade, str(grade))
    
    def test_student_default_grade(self):
        """Test student grade defaults to '1'"""
        student = Student.objects.create(
            school_name='Test School'
        )
        
        self.assertEqual(student.student_grade, '1')
    
    def test_student_whatsapp_opt_in_default(self):
        """Test whatsapp_opt_in defaults to None"""
        student = Student.objects.create(
            user=self.user,
            school_name='Test School',
            student_grade='5'
        )
        
        self.assertIsNone(student.whatsapp_opt_in)
    
    def test_student_whatsapp_group_url(self):
        """Test whatsapp_group_url field"""
        student = Student.objects.create(
            user=self.user,
            school_name='Test School',
            student_grade='5',
            whatsapp_group_url='https://chat.whatsapp.com/test'
        )
        
        self.assertEqual(student.whatsapp_group_url, 'https://chat.whatsapp.com/test')
    
    def test_student_auto_charge_default(self):
        """Test auto_charge defaults to 'no'"""
        student = Student.objects.create(
            user=self.user,
            school_name='Test School',
            student_grade='5'
        )
        
        self.assertEqual(student.auto_charge, 'no')
    
    def test_student_enrolled_default(self):
        """Test enrolled defaults to False"""
        student = Student.objects.create(
            user=self.user,
            school_name='Test School',
            student_grade='5'
        )
        
        self.assertFalse(student.enrolled)
    
    def test_student_account_status_default(self):
        """Test account_status defaults to 'active'"""
        student = Student.objects.create(
            user=self.user,
            school_name='Test School',
            student_grade='5'
        )
        
        self.assertEqual(student.account_status, 'active')
    
    def test_student_account_status_choices(self):
        """Test account_status field choices"""
        for status in ['active', 'inactive', 'duePayment']:
            student = Student.objects.create(
                user=self.user,
                school_name='Test School',
                student_grade='5',
                account_status=status
            )
            self.assertEqual(student.account_status, status)
    
    def test_student_created_by(self):
        """Test created_by field"""
        admin_user = User.objects.create_user(
            username='admin',
            email='admin@test.com',
            password='TestPass123!',
            user_type='admin'
        )
        
        student = Student.objects.create(
            user=self.user,
            school_name='Test School',
            student_grade='5',
            created_by=admin_user
        )
        
        self.assertEqual(student.created_by, admin_user)
    
    def test_student_relationship_manager(self):
        """Test relationship_manager field"""
        admin_user = User.objects.create_user(
            username='admin',
            email='admin@test.com',
            password='TestPass123!',
            user_type='admin'
        )
        
        student = Student.objects.create(
            user=self.user,
            school_name='Test School',
            student_grade='5',
            relationship_manager=admin_user
        )
        
        self.assertEqual(student.relationship_manager, admin_user)
    
    def test_student_signup_source(self):
        """Test signup_source field"""
        student = Student.objects.create(
            user=self.user,
            school_name='Test School',
            student_grade='5',
            signup_source='google_ads'
        )
        
        self.assertEqual(student.signup_source, 'google_ads')
