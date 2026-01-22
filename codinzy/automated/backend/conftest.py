"""
Pytest Configuration and Shared Fixtures for Codinzy Backend Tests

This module provides:
- Database setup and teardown fixtures
- User authentication fixtures
- Test data generation utilities
"""

import pytest
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from datetime import datetime, timedelta
from faker import Faker

from api.models import (
    User, Teacher, Student, Course, Module, Lesson,
    ScheduledClass, ClassroomSession, Batch,
    Lead, Payment, Enrollment, Quiz, Badge,
    Certificate, CreditTransaction, TeacherAvailability,
    ClassActivity, AfterClassProject, StudentActivitySubmission,
    DiscountCode, StudentBilling, SiteSettings,
    UTMTracking, AutoLoginLink
)

fake = Faker()


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    """Enable database access for all tests by default"""
    pass


@pytest.fixture
def test_user(db):
    """Create a basic test user"""
    user = User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123',
        name='Test User',
        user_type='student'
    )
    return user


@pytest.fixture
def test_student(db):
    """Create a test student with user profile"""
    user = User.objects.create_user(
        username='student_test',
        email='student@test.com',
        password='studentpass123',
        name='Test Student',
        user_type='student'
    )
    student = Student.objects.create(
        user=user,
        school_name='Test School',
        student_grade='5',
        state='Test State'
    )
    return student


@pytest.fixture
def test_teacher(db):
    """Create a test teacher with user profile"""
    user = User.objects.create_user(
        username='teacher_test',
        email='teacher@test.com',
        password='teacherpass123',
        name='Test Teacher',
        user_type='teacher'
    )
    teacher = Teacher.objects.create(
        user=user,
        details='Test teacher details',
        qualification='Masters in Computer Science',
        experience_years='5'
    )
    return teacher


@pytest.fixture
def test_admin(db):
    """Create a test admin user"""
    user = User.objects.create_user(
        username='admin_test',
        email='admin@test.com',
        password='adminpass123',
        name='Test Admin',
        user_type='admin',
        is_staff=True,
        is_superuser=True
    )
    return user


@pytest.fixture
def test_users(db):
    """Create multiple test users of different types"""
    users = {}
    
    student_user = User.objects.create_user(
        username='student_user',
        email='student@example.com',
        password='student123',
        name='Student User',
        user_type='student'
    )
    users['student'] = student_user
    
    teacher_user = User.objects.create_user(
        username='teacher_user',
        email='teacher@example.com',
        password='teacher123',
        name='Teacher User',
        user_type='teacher'
    )
    users['teacher'] = teacher_user
    
    admin_user = User.objects.create_user(
        username='admin_user',
        email='admin@example.com',
        password='admin123',
        name='Admin User',
        user_type='admin',
        is_staff=True
    )
    users['admin'] = admin_user
    
    return users


@pytest.fixture
def api_client():
    """Create an API client for testing"""
    return APIClient()


@pytest.fixture
def authenticated_client(db, test_user):
    """Create an authenticated API client"""
    client = APIClient()
    token = Token.objects.create(user=test_user)
    client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    return client


@pytest.fixture
def student_client(db, test_student):
    """Create an authenticated client for student"""
    client = APIClient()
    token = Token.objects.create(user=test_student.user)
    client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    return client


@pytest.fixture
def teacher_client(db, test_teacher):
    """Create an authenticated client for teacher"""
    client = APIClient()
    token = Token.objects.create(user=test_teacher.user)
    client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    return client


@pytest.fixture
def admin_client(db, test_admin):
    """Create an authenticated client for admin"""
    client = APIClient()
    token = Token.objects.create(user=test_admin)
    client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    return client


@pytest.fixture
def test_course(db, test_teacher):
    """Create a test course"""
    course = Course.objects.create(
        title='Test Python Course',
        description='A test course for unit testing',
        language='Python',
        difficulty_level='beginner',
        created_by=test_teacher.user,
        is_active=True
    )
    return course


@pytest.fixture
def test_module(db, test_course):
    """Create a test module"""
    module = Module.objects.create(
        course=test_course,
        title='Test Module 1',
        description='First test module',
        order=1
    )
    return module


@pytest.fixture
def test_lesson(db, test_module):
    """Create a test lesson"""
    lesson = Lesson.objects.create(
        lesson_code=f'LESSON-{fake.unique.random_number(digits=4)}',
        lesson_name='Test Lesson',
        description='A test lesson',
        module=test_module,
        order=1,
        duration_minutes=30
    )
    return lesson


@pytest.fixture
def test_scheduled_class(db, test_course, test_teacher, test_student):
    """Create a test scheduled class"""
    scheduled_class = ScheduledClass.objects.create(
        course=test_course,
        teacher=test_teacher,
        scheduled_start_time=datetime.now() + timedelta(days=1),
        scheduled_end_time=datetime.now() + timedelta(days=1, hours=1),
        title='Test Scheduled Class',
        status='scheduled',
        class_method='jitsi',
        timezone='UTC'
    )
    scheduled_class.students.add(test_student)
    return scheduled_class


@pytest.fixture
def test_lead(db):
    """Create a test lead"""
    lead = Lead.objects.create(
        parent_name='Test Parent',
        student_name='Test Student',
        student_grade='5',
        email='lead@test.com',
        phone='+1234567890',
        country='US',
        timezone='America/New_York',
        stage='new',
        source='website'
    )
    return lead


@pytest.fixture
def test_payment(db, test_student, test_course):
    """Create a test payment"""
    payment = Payment.objects.create(
        student=test_student,
        course=test_course,
        amount=100.00,
        status='pending',
        payment_method='stripe',
        currency='USD'
    )
    return payment


@pytest.fixture
def test_badge(db):
    """Create a test badge"""
    badge = Badge.objects.create(
        name='Test Badge',
        description='A test badge',
        icon='test-icon.png',
        xp_points=50,
        category='achievement',
        criteria={'tests_completed': 5}
    )
    return badge


@pytest.fixture
def test_certificate(db, test_student, test_course):
    """Create a test certificate"""
    cert = Certificate.objects.create(
        student=test_student,
        course=test_course,
        certificate_number='CERT-TEST-001',
        issue_date='2026-01-20',
        pdf_url='/certificates/test.pdf'
    )
    return cert


def create_test_user_with_token(user_type='student'):
    """Helper to create user with authentication token"""
    user = User.objects.create_user(
        username=f'test_{user_type}_{fake.unique.random_number()}',
        email=f'{user_type}_{fake.unique.random_number()}@test.com',
        password='testpass123',
        name=f'Test {user_type.title()}',
        user_type=user_type
    )
    token = Token.objects.create(user=user)
    return user, token


def create_multiple_students(count=5):
    """Create multiple test students"""
    students = []
    for i in range(count):
        user = User.objects.create_user(
            username=f'student_{i}_{fake.random_number()}',
            email=f'student_{i}@test.com',
            password='testpass123',
            name=f'Student {i}',
            user_type='student'
        )
        student = Student.objects.create(
            user=user,
            school_name='Test School',
            student_grade=f'{fake.random_digit_not_null()}'
        )
        students.append(student)
    return students


def create_multiple_courses(count=3):
    """Create multiple test courses"""
    courses = []
    for i in range(count):
        course = Course.objects.create(
            title=f'Test Course {i}',
            description=f'Description for course {i}',
            language=fake.random_element(['Python', 'JavaScript', 'Scratch']),
            difficulty_level='beginner',
            is_active=True
        )
        courses.append(course)
    return courses
