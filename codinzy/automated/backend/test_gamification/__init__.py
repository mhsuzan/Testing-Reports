"""
Gamification Test Suite for Codinzy Backend

Tests cover:
- Badge awarding and tracking
- XP points system
- Leaderboard calculations
- Student achievements
"""

import pytest
from datetime import datetime, timedelta, date
from decimal import Decimal
from rest_framework.test import APITestCase

import sys
from pathlib import Path
backend_path = Path(__file__).parent.parent.parent.parent / 'backend'
sys.path.insert(0, str(backend_path))

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_settings')

import django
django.setup()

from api.models import User, Badge, Certificate, StudentBadge, GamificationPoint, GamificationAchievement, GamificationLeaderboard, LeaderboardEntry, Student, Teacher, Course
from django.db import models


class BadgeModelTestCase(APITestCase):
    """Test cases for Badge model"""
    
    def test_badge_creation(self):
        """Test badge creation"""
        badge = Badge.objects.create(
            name='Great Job',
            emoji='🌟',
            description='Awarded for excellent work',
            color='#FFD700'
        )
        
        self.assertIsNotNone(badge)
        self.assertEqual(badge.name, 'Great Job')
        self.assertEqual(badge.emoji, '🌟')
    
    def test_badge_str_representation(self):
        """Test badge string representation"""
        badge = Badge.objects.create(
            name='Perfect Score',
            emoji='💯'
        )
        
        expected = f"💯 Perfect Score"
        self.assertEqual(str(badge), expected)
    
    def test_badge_name_unique(self):
        """Test badge name must be unique"""
        Badge.objects.create(
            name='Unique Badge',
            emoji='⭐'
        )
        
        with self.assertRaises(Exception):
            Badge.objects.create(
                name='Unique Badge',
                emoji='🏅'
            )
    
    def test_badge_default_color(self):
        """Test badge default color is gold"""
        badge = Badge.objects.create(
            name='Test Badge',
            emoji='🎯'
        )
        
        self.assertEqual(badge.color, '#FFD700')
    
    def test_badge_is_active_default(self):
        """Test badge is_active defaults to True"""
        badge = Badge.objects.create(
            name='Test Badge',
            emoji='🎯'
        )
        
        self.assertTrue(badge.is_active)


class StudentBadgeTestCase(APITestCase):
    """Test cases for StudentBadge model"""
    
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
        self.teacher = Teacher.objects.create(
            user=self.teacher_user,
            details='Test teacher'
        )
        
        self.badge = Badge.objects.create(
            name='Great Job',
            emoji='🌟'
        )
    
    def test_student_badge_awarding(self):
        """Test badge can be awarded to student"""
        student_badge = StudentBadge.objects.create(
            student=self.student,
            teacher=self.teacher,
            badge=self.badge
        )
        
        self.assertIsNotNone(student_badge)
        self.assertEqual(student_badge.student, self.student)
        self.assertEqual(student_badge.badge, self.badge)
    
    def test_student_badge_str_representation(self):
        """Test student badge string representation"""
        student_badge = StudentBadge.objects.create(
            student=self.student,
            teacher=self.teacher,
            badge=self.badge
        )
        
        self.assertIn('Great Job', str(student_badge))


class GamificationPointTestCase(APITestCase):
    """Test cases for GamificationPoint model"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='student',
            email='student@test.com',
            password='TestPass123!',
            user_type='student',
            name='Test Student'
        )
    
    def test_gamification_point_creation(self):
        """Test gamification point creation"""
        point = GamificationPoint.objects.create(
            user=self.user,
            point_type='class_attendance',
            points=10,
            description='Attended class'
        )
        
        self.assertIsNotNone(point)
        self.assertEqual(point.points, 10)
        self.assertEqual(point.point_type, 'class_attendance')
    
    def test_gamification_point_type_choices(self):
        """Test point_type field choices"""
        for point_type in ['class_attendance', 'project_submission', 'badge_earned', 'streak_bonus']:
            point = GamificationPoint.objects.create(
                user=self.user,
                point_type=point_type,
                points=5
            )
            self.assertEqual(point.point_type, point_type)
    
    def test_gamification_point_str_representation(self):
        """Test gamification point string representation"""
        point = GamificationPoint.objects.create(
            user=self.user,
            point_type='class_attendance',
            points=5
        )
        
        self.assertIn('Test Student', str(point))
    
    def test_total_xp_calculation(self):
        """Test total XP calculation for user"""
        GamificationPoint.objects.create(
            user=self.user,
            point_type='class_attendance',
            points=10
        )
        GamificationPoint.objects.create(
            user=self.user,
            point_type='project_submission',
            points=20
        )
        
        total = GamificationPoint.objects.filter(user=self.user).aggregate(
            total=models.Sum('points')
        )['total'] or 0
        
        self.assertEqual(total, 30)


class GamificationAchievementTestCase(APITestCase):
    """Test cases for GamificationAchievement model"""
    
    def test_gamification_achievement_creation(self):
        """Test gamification achievement creation"""
        achievement = GamificationAchievement.objects.create(
            achievement_type='attendance',
            name='Perfect Attendance',
            description='Attended all classes for a month',
            icon='🏆',
            color='#FFD700'
        )
        
        self.assertIsNotNone(achievement)
        self.assertEqual(achievement.achievement_type, 'attendance')
        self.assertEqual(achievement.name, 'Perfect Attendance')


class LeaderboardEntryTestCase(APITestCase):
    """Test cases for LeaderboardEntry model"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='student',
            email='student@test.com',
            password='TestPass123!',
            user_type='student',
            name='Test Student'
        )
        
        self.leaderboard = GamificationLeaderboard.objects.create(
            leaderboard_type='weekly',
            period_start=date.today(),
            period_end=date.today() + timedelta(days=7)
        )
    
    def test_leaderboard_entry_creation(self):
        """Test leaderboard entry creation"""
        entry = LeaderboardEntry.objects.create(
            leaderboard=self.leaderboard,
            user=self.user,
            total_points=500,
            position=1
        )
        
        self.assertIsNotNone(entry)
        self.assertEqual(entry.total_points, 500)
        self.assertEqual(entry.position, 1)


class CertificateModelTestCase(APITestCase):
    """Test cases for Certificate model"""
    
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
        
        self.course = Course.objects.create(
            title='Python Course',
            description='Learn Python',
            course_code='PY'
        )
    
    def test_certificate_creation(self):
        """Test certificate creation"""
        cert = Certificate.objects.create(
            certificate_id='CERT-001',
            student=self.student,
            course=self.course,
            certificate_type='module_completion',
            student_name='Test Student',
            completion_date=datetime.now().date()
        )
        
        self.assertIsNotNone(cert)
        self.assertEqual(cert.student, self.student)
        self.assertEqual(cert.certificate_id, 'CERT-001')
    
    def test_certificate_str_representation(self):
        """Test certificate string representation"""
        cert = Certificate.objects.create(
            certificate_id='CERT-002',
            student=self.student,
            course=self.course,
            certificate_type='module_completion',
            student_name='Test Student',
            completion_date=datetime.now().date()
        )
        
        self.assertIn('Test Student', str(cert))
