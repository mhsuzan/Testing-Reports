"""
Lead Management Test Suite for Codinzy Backend

Tests cover:
- Lead model validation
- Lead stage transitions
- Lead activity tracking
- Trial class booking flow
- Lead assignment and management
"""

import pytest
from datetime import datetime, timedelta
from django.db import IntegrityError
from rest_framework.test import APITestCase

import sys
from pathlib import Path
backend_path = Path(__file__).parent.parent.parent.parent / 'backend'
sys.path.insert(0, str(backend_path))

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_settings')

import django
django.setup()

from api.models import User, Lead, LeadActivity, TrialClassHistory, TrialClassSetting, Student, Course, Teacher


class LeadModelTestCase(APITestCase):
    """Test cases for Lead model"""
    
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
        
        self.owner_user = User.objects.create_user(
            username='sales',
            email='sales@test.com',
            password='TestPass123!',
            user_type='admin',
            name='Sales Person'
        )
    
    def test_lead_creation_minimal(self):
        """Test lead creation with minimal data"""
        lead = Lead.objects.create(
            student=self.student
        )
        
        self.assertIsNotNone(lead)
        self.assertEqual(lead.stage, 'new')
        self.assertIsNone(lead.owner)
    
    def test_lead_full_creation(self):
        """Test lead creation with all fields"""
        lead = Lead.objects.create(
            student=self.student,
            owner=self.owner_user,
            lead_source='website',
            lead_score=75
        )
        
        self.assertIsNotNone(lead)
        self.assertEqual(lead.lead_source, 'website')
        self.assertEqual(lead.lead_score, 75)
    
    def test_lead_stage_choices(self):
        """Test lead stage field choices"""
        for stage in ['new', 'contacted', 'trial_booked', 'trial_complete', 'won', 'lost']:
            lead = Lead.objects.create(
                student=self.student,
                stage=stage
            )
            self.assertEqual(lead.stage, stage)
    
    def test_lead_str_representation(self):
        """Test lead string representation"""
        lead = Lead.objects.create(
            student=self.student
        )
        
        self.assertIn('Test Student', str(lead))
    
    def test_lead_source_choices(self):
        """Test lead_source field"""
        lead = Lead.objects.create(
            student=self.student,
            lead_source='referral'
        )
        
        self.assertEqual(lead.lead_source, 'referral')
    
    def test_lead_timestamp_fields(self):
        """Test lead timestamp fields are set"""
        lead = Lead.objects.create(
            student=self.student
        )
        
        self.assertIsNotNone(lead.created_at)
        self.assertIsNotNone(lead.updated_at)
    
    def test_lead_lead_score_default(self):
        """Test lead_score defaults to 0"""
        lead = Lead.objects.create(
            student=self.student
        )
        
        self.assertEqual(lead.lead_score, 0)


class LeadStageTransitionTestCase(APITestCase):
    """Test cases for Lead stage transitions"""
    
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
    
    def test_new_to_trial_scheduled(self):
        """Test lead can transition from new to trial_booked"""
        lead = Lead.objects.create(
            student=self.student,
            stage='new'
        )
        
        lead.stage = 'trial_booked'
        lead.save()
        
        self.assertEqual(lead.stage, 'trial_booked')
    
    def test_trial_scheduled_to_trial_complete(self):
        """Test lead can transition from trial_booked to trial_complete"""
        lead = Lead.objects.create(
            student=self.student,
            stage='trial_booked'
        )
        
        lead.stage = 'trial_complete'
        lead.save()
        
        self.assertEqual(lead.stage, 'trial_complete')
    
    def test_trial_complete_to_enrolled(self):
        """Test lead can transition from trial_complete to won"""
        lead = Lead.objects.create(
            student=self.student,
            stage='trial_complete'
        )
        
        lead.stage = 'won'
        lead.save()
        
        self.assertEqual(lead.stage, 'won')
    
    def test_trial_scheduled_to_trial_absent(self):
        """Test lead can transition from trial_booked to trial_absent"""
        lead = Lead.objects.create(
            student=self.student,
            stage='trial_booked'
        )
        
        lead.stage = 'trial_absent'
        lead.save()
        
        self.assertEqual(lead.stage, 'trial_absent')
    
    def test_any_stage_to_lost(self):
        """Test lead can transition from any stage to lost"""
        for initial_stage in ['new', 'contacted', 'trial_booked', 'trial_complete']:
            lead = Lead.objects.create(
                student=self.student,
                stage=initial_stage
            )
            lead.stage = 'lost'
            lead.save()
            
            self.assertEqual(lead.stage, 'lost')


class LeadAssignmentTestCase(APITestCase):
    """Test cases for Lead assignment"""
    
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
        
        self.owner_user = User.objects.create_user(
            username='sales1',
            email='sales1@test.com',
            password='TestPass123!',
            user_type='admin',
            name='Sales Person 1'
        )
    
    def test_lead_assignment(self):
        """Test lead can be assigned to an owner"""
        lead = Lead.objects.create(
            student=self.student,
            owner=self.owner_user
        )
        
        self.assertEqual(lead.owner, self.owner_user)
    
    def test_lead_assignment_none(self):
        """Test lead can have no owner"""
        lead = Lead.objects.create(
            student=self.student,
            owner=None
        )
        
        self.assertIsNone(lead.owner)
    
    def test_lead_assignment_change(self):
        """Test lead owner can be changed"""
        owner2 = User.objects.create_user(
            username='sales2',
            email='sales2@test.com',
            password='TestPass123!',
            user_type='admin',
            name='Sales Person 2'
        )
        
        lead = Lead.objects.create(
            student=self.student,
            owner=self.owner_user
        )
        
        lead.owner = owner2
        lead.save()
        
        self.assertEqual(lead.owner, owner2)


class LeadActivityTestCase(APITestCase):
    """Test cases for LeadActivity model"""
    
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
        
        self.lead = Lead.objects.create(
            student=self.student
        )
    
    def test_lead_activity_creation(self):
        """Test lead activity creation"""
        activity = LeadActivity.objects.create(
            lead=self.lead,
            activity_type='call',
            description='Follow-up call'
        )
        
        self.assertIsNotNone(activity)
        self.assertEqual(activity.activity_type, 'call')
    
    def test_lead_activity_relationship(self):
        """Test lead activity belongs to lead"""
        activity = LeadActivity.objects.create(
            lead=self.lead,
            activity_type='email',
            description='Sent email'
        )
        
        self.assertIn(activity, self.lead.activities.all())


class TrialClassSettingTestCase(APITestCase):
    """Test cases for TrialClassSetting model"""
    
    def setUp(self):
        """Set up test data"""
        teacher_user = User.objects.create_user(
            username='teacher',
            email='teacher@test.com',
            password='TestPass123!',
            user_type='teacher',
            name='Test Teacher'
        )
        self.teacher = Teacher.objects.create(
            user=teacher_user,
            details='Test teacher'
        )
    
    def test_trial_class_setting_creation(self):
        """Test trial class setting creation"""
        setting = TrialClassSetting.objects.create(
            teacher=self.teacher
        )
        
        self.assertIsNotNone(setting)
        self.assertEqual(setting.teacher, self.teacher)
    
    def test_trial_class_setting_ordering(self):
        """Test trial class settings are ordered"""
        setting1 = TrialClassSetting.objects.create(
            teacher=self.teacher
        )
        setting2 = TrialClassSetting.objects.create(
            teacher=self.teacher
        )
        
        settings = list(TrialClassSetting.objects.all())
        self.assertEqual(len(settings), 2)
