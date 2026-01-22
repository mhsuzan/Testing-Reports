"""
Communications Tests for Codinzy Backend

Tests cover:
- Email service integration
- WhatsApp message tracking
- Notification preferences
"""

import pytest
from rest_framework.test import APITestCase

import sys
from pathlib import Path
backend_path = Path(__file__).parent.parent.parent.parent / 'backend'
sys.path.insert(0, str(backend_path))

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_settings')

import django
django.setup()

from api.models import User, Student, UTMTracking, AutoLoginLink


class EmailServiceTestCase(APITestCase):
    """Test cases for email service"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='student',
            email='student@test.com',
            password='TestPass123!',
            user_type='student',
            name='Test Student'
        )
    
    def test_user_email_field(self):
        """Test user has email field"""
        self.assertEqual(self.user.email, 'student@test.com')
    
    def test_user_email_unique(self):
        """Test email must be unique"""
        with self.assertRaises(Exception):
            User.objects.create_user(
                username='student2',
                email='student@test.com',
                password='TestPass123!'
            )


class WhatsAppTrackingTestCase(APITestCase):
    """Test cases for WhatsApp tracking"""
    
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
    
    def test_student_whatsapp_opt_in(self):
        """Test student can have WhatsApp opt-in"""
        self.student.whatsapp_opt_in = True
        self.student.save()
        
        self.student.refresh_from_db()
        self.assertTrue(self.student.whatsapp_opt_in)
    
    def test_student_whatsapp_group_url(self):
        """Test student can have WhatsApp group URL"""
        self.student.whatsapp_group_url = 'https://chat.whatsapp.com/abc123'
        self.student.save()
        
        self.student.refresh_from_db()
        self.assertEqual(self.student.whatsapp_group_url, 'https://chat.whatsapp.com/abc123')


class UTMTrackingTestCase(APITestCase):
    """Test cases for UTM tracking"""
    
    def test_utm_tracking_creation(self):
        """Test UTM tracking creation"""
        utm = UTMTracking.objects.create(
            name='Winter Campaign',
            utm_source='google',
            utm_medium='cpc',
            utm_campaign='winter_2024'
        )
        
        self.assertIsNotNone(utm)
        self.assertEqual(utm.utm_source, 'google')
    
    def test_utm_tracking_str(self):
        """Test UTM tracking string representation"""
        utm = UTMTracking.objects.create(
            name='Test Campaign',
            utm_source='facebook',
            utm_medium='social'
        )
        
        self.assertIn('Test Campaign', str(utm))


class AutoLoginLinkTestCase(APITestCase):
    """Test cases for auto-login links"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='student',
            email='student@test.com',
            password='TestPass123!',
            user_type='student',
            name='Test Student'
        )
    
    def test_auto_login_link_creation(self):
        """Test auto-login link creation"""
        link = AutoLoginLink.objects.create(
            user=self.user
        )
        
        self.assertIsNotNone(link)
        self.assertIsNotNone(link.token)
        self.assertEqual(len(link.token), 32)
    
    def test_auto_login_link_expiration(self):
        """Test auto-login link has expiration"""
        from datetime import timedelta
        
        link = AutoLoginLink.objects.create(
            user=self.user,
            expires_at=link.created_at + timedelta(hours=24)
        )
        
        self.assertIsNotNone(link.expires_at)
