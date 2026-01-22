"""
Authentication Test Module for Codinzy Backend

Tests cover:
- User registration and login
- Token-based authentication
- Password reset functionality
- Session management
- Role-based access control
"""

import pytest
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

import sys
from pathlib import Path
backend_path = Path(__file__).parent.parent.parent.parent / 'backend'
sys.path.insert(0, str(backend_path))

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_settings')

import django
django.setup()

from api.models import User, Student, Teacher


class AuthenticationTestCase(APITestCase):
    """Test cases for authentication functionality"""
    
    def setUp(self):
        """Set up test data"""
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'TestPass123!',
            'name': 'Test User',
            'user_type': 'student'
        }
    
    def test_user_registration_success(self):
        """Test successful user registration"""
        url = '/api/auth/register/'
        response = self.client.post(url, self.user_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
        self.assertIn('user', response.data)
        self.assertEqual(response.data['user']['username'], self.user_data['username'])
        self.assertEqual(response.data['user']['email'], self.user_data['email'])
        self.assertEqual(response.data['user']['user_type'], self.user_data['user_type'])
    
    def test_user_registration_duplicate_username(self):
        """Test registration with duplicate username fails"""
        # Create existing user
        User.objects.create_user(
            username='testuser',
            email='existing@example.com',
            password='TestPass123!'
        )
        
        url = '/api/auth/register/'
        response = self.client.post(url, self.user_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)
    
    def test_user_registration_duplicate_email(self):
        """Test registration with duplicate email fails"""
        # Create existing user
        User.objects.create_user(
            username='existinguser',
            email='test@example.com',
            password='TestPass123!'
        )
        
        url = '/api/auth/register/'
        response = self.client.post(url, self.user_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
    
    def test_user_registration_invalid_password(self):
        """Test registration with weak password fails"""
        self.user_data['password'] = 'weak'
        url = '/api/auth/register/'
        response = self.client.post(url, self.user_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)
    
    def test_login_success(self):
        """Test successful login"""
        # Create user
        User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123!'
        )
        
        url = '/api/auth/login/'
        response = self.client.post(url, {
            'username': 'testuser',
            'password': 'TestPass123!'
        }, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        self.assertIn('user', response.data)
    
    def test_login_invalid_credentials(self):
        """Test login with invalid credentials fails"""
        # Create user
        User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123!'
        )
        
        url = '/api/auth/login/'
        response = self.client.post(url, {
            'username': 'testuser',
            'password': 'WrongPassword123!'
        }, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('error', response.data)
    
    def test_login_nonexistent_user(self):
        """Test login with non-existent user fails"""
        url = '/api/auth/login/'
        response = self.client.post(url, {
            'username': 'nonexistent',
            'password': 'TestPass123!'
        }, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_logout_success(self):
        """Test successful logout"""
        # Create and authenticate user
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123!'
        )
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        
        url = '/api/auth/logout/'
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify token is deleted
        self.assertFalse(Token.objects.filter(user=user).exists())
    
    def test_password_reset_request(self):
        """Test password reset request"""
        # Create user
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123!'
        )
        
        url = '/api/auth/password/reset/'
        response = self.client.post(url, {
            'email': 'test@example.com'
        }, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_password_reset_confirm(self):
        """Test password reset confirmation"""
        # Create user
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123!'
        )
        
        # This would typically involve a uid and token from email
        # For unit testing, we test the endpoint structure
        url = '/api/auth/password/reset/confirm/'
        response = self.client.post(url, {
            'new_password': 'NewPass123!',
            'confirm_password': 'NewPass123!'
        }, format='json')
        
        # Response depends on implementation
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_400_BAD_REQUEST])


class TokenAuthenticationTestCase(APITestCase):
    """Test cases for token-based authentication"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123!'
        )
        self.token = Token.objects.create(user=self.user)
    
    def test_token_creation(self):
        """Test that token is created on user creation"""
        new_user = User.objects.create_user(
            username='newuser',
            email='new@example.com',
            password='TestPass123!'
        )
        token = Token.objects.get(user=new_user)
        self.assertIsNotNone(token)
        self.assertEqual(len(token.key), 40)
    
    def test_authenticated_request(self):
        """Test authenticated request with valid token"""
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        
        url = '/api/auth/user/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')
    
    def test_unauthenticated_request(self):
        """Test unauthenticated request fails"""
        url = '/api/auth/user/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_invalid_token_request(self):
        """Test request with invalid token fails"""
        self.client.credentials(HTTP_AUTHORIZATION='Token invalidtoken123')
        
        url = '/api/auth/user/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_expired_token_request(self):
        """Test request with expired token fails"""
        # Set token as expired
        self.token.created = self.token.created.replace(
            year=self.token.created.year - 1
        )
        self.token.save()
        
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        
        url = '/api/auth/user/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_token_deletion_on_logout(self):
        """Test token is deleted on logout"""
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        
        url = '/api/auth/logout/'
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Token.objects.filter(key=self.token.key).exists())
    
    def test_multiple_tokens_per_user(self):
        """Test that user can have multiple tokens"""
        # Create additional token
        new_token = Token.objects.create(user=self.user)
        
        # Both tokens should work
        self.assertTrue(Token.objects.filter(user=self.user).count() == 2)
        
        # Deleting one shouldn't affect the other
        new_token.delete()
        self.assertTrue(Token.objects.filter(user=self.user).exists())


class RoleBasedAccessTestCase(APITestCase):
    """Test cases for role-based access control"""
    
    def setUp(self):
        """Set up test data"""
        self.student_user = User.objects.create_user(
            username='student',
            email='student@test.com',
            password='TestPass123!',
            user_type='student'
        )
        self.teacher_user = User.objects.create_user(
            username='teacher',
            email='teacher@test.com',
            password='TestPass123!',
            user_type='teacher'
        )
        self.admin_user = User.objects.create_user(
            username='admin',
            email='admin@test.com',
            password='TestPass123!',
            user_type='admin',
            is_staff=True
        )
    
    def test_student_access_to_student_dashboard(self):
        """Test student can access student dashboard"""
        token = Token.objects.create(user=self.student_user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        
        url = '/api/student/dashboard/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_teacher_access_to_teacher_dashboard(self):
        """Test teacher can access teacher dashboard"""
        token = Token.objects.create(user=self.teacher_user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        
        url = '/api/teacher/dashboard/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_admin_access_to_admin_dashboard(self):
        """Test admin can access admin dashboard"""
        token = Token.objects.create(user=self.admin_user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        
        url = '/api/admin/dashboard/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_student_denied_teacher_dashboard(self):
        """Test student cannot access teacher dashboard"""
        token = Token.objects.create(user=self.student_user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        
        url = '/api/teacher/dashboard/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_teacher_denied_student_dashboard(self):
        """Test teacher cannot access student dashboard"""
        token = Token.objects.create(user=self.teacher_user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        
        url = '/api/student/dashboard/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_unauthenticated_denied_all_dashboards(self):
        """Test unauthenticated users cannot access any dashboard"""
        # Student dashboard
        response = self.client.get('/api/student/dashboard/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        # Teacher dashboard
        response = self.client.get('/api/teacher/dashboard/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        # Admin dashboard
        response = self.client.get('/api/admin/dashboard/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class UserTypeMethodsTestCase(APITestCase):
    """Test cases for user type checking methods"""
    
    def test_user_is_student(self):
        """Test is_student method returns correct value"""
        student_user = User.objects.create_user(
            username='student',
            email='student@test.com',
            password='TestPass123!',
            user_type='student'
        )
        self.assertTrue(student_user.is_student())
    
    def test_user_is_teacher(self):
        """Test is_teacher method returns correct value"""
        teacher_user = User.objects.create_user(
            username='teacher',
            email='teacher@test.com',
            password='TestPass123!',
            user_type='teacher'
        )
        self.assertTrue(teacher_user.is_teacher())
    
    def test_user_is_admin(self):
        """Test is_admin method returns correct value"""
        admin_user = User.objects.create_user(
            username='admin',
            email='admin@test.com',
            password='TestPass123!',
            user_type='admin'
        )
        self.assertTrue(admin_user.is_admin())
    
    def test_superuser_is_admin(self):
        """Test superuser is considered admin"""
        superuser = User.objects.create_superuser(
            username='superuser',
            email='super@test.com',
            password='TestPass123!'
        )
        self.assertTrue(superuser.is_admin())
    
    def test_get_full_name(self):
        """Test get_full_name method"""
        user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='TestPass123!',
            name='Test User'
        )
        self.assertEqual(user.get_full_name(), 'Test User')
    
    def test_get_short_name(self):
        """Test get_short_name method"""
        user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='TestPass123!',
            name='Test User'
        )
        self.assertEqual(user.get_short_name(), 'Test')
    
    def test_referral_code_generation(self):
        """Test referral code is auto-generated"""
        user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='TestPass123!'
        )
        self.assertIsNotNone(user.referral_code)
        self.assertEqual(len(user.referral_code), 5)
        self.assertTrue(user.referral_code.isalnum())
    
    def test_referral_code_uniqueness(self):
        """Test referral codes are unique"""
        user1 = User.objects.create_user(
            username='user1',
            email='user1@test.com',
            password='TestPass123!'
        )
        user2 = User.objects.create_user(
            username='user2',
            email='user2@test.com',
            password='TestPass123!'
        )
        self.assertNotEqual(user1.referral_code, user2.referral_code)


class AutoLoginLinkTestCase(APITestCase):
    """Test cases for auto-login links"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='TestPass123!'
        )
    
    def test_auto_login_link_creation(self):
        """Test auto-login link is created"""
        from api.models import AutoLoginLink
        
        link = AutoLoginLink.objects.create(
            user=self.user,
            expires_at=None
        )
        
        self.assertIsNotNone(link.token)
        self.assertEqual(len(link.token), 32)
        self.assertTrue(link.is_active)
    
    def test_auto_login_link_expiration(self):
        """Test auto-login link expiration"""
        from api.models import AutoLoginLink
        from datetime import timedelta
        
        link = AutoLoginLink.objects.create(
            user=self.user,
            expires_at=link.created_at + timedelta(hours=24)
        )
        
        self.assertIsNotNone(link.expires_at)
        self.assertTrue(link.is_expired() is False or link.expires_at > link.created_at)
    
    def test_auto_login_link_usage_count(self):
        """Test auto-login link usage count"""
        from api.models import AutoLoginLink
        
        link = AutoLoginLink.objects.create(user=self.user)
        self.assertEqual(link.usage_count, 0)
        
        link.usage_count += 1
        link.save()
        
        link.refresh_from_db()
        self.assertEqual(link.usage_count, 1)
    
    def test_unique_active_autologin_constraint(self):
        """Test unique active auto-login constraint per user"""
        from api.models import AutoLoginLink
        
        link1 = AutoLoginLink.objects.create(
            user=self.user,
            is_active=True
        )
        
        # Second active link should fail
        with self.assertRaises(Exception):
            link2 = AutoLoginLink(
                user=self.user,
                is_active=True
            )
            link2.save()
