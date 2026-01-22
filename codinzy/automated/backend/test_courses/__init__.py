"""
Course and Lesson Model Tests for Codinzy Backend

Tests cover:
- Course CRUD operations
- Module management
- Lesson management
- Course enrollment
"""

import pytest
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

from api.models import User, Course, Module, Lesson, Batch, Enrollment, CourseModuleOrder, ModuleLessonOrder, Teacher, Student


class CourseModelTestCase(APITestCase):
    """Test cases for Course model"""
    
    def setUp(self):
        """Set up test data"""
        self.teacher = User.objects.create_user(
            username='teacher',
            email='teacher@test.com',
            password='TestPass123!',
            user_type='teacher',
            name='Test Teacher'
        )
    
    def test_course_creation(self):
        """Test course creation"""
        course = Course.objects.create(
            title='Python Basics',
            description='Learn Python programming',
            course_code='PY101',
            created_by=self.teacher
        )
        
        self.assertIsNotNone(course)
        self.assertEqual(course.title, 'Python Basics')
        self.assertEqual(course.course_code, 'PY101')
        self.assertEqual(course.description, 'Learn Python programming')
    
    def test_course_str_representation(self):
        """Test course string representation"""
        course = Course.objects.create(
            title='Python Basics',
            description='Learn Python',
            course_code='PY101'
        )
        
        self.assertEqual(str(course), 'Python Basics')
    
    def test_course_code_unique(self):
        """Test course code must be unique"""
        Course.objects.create(
            title='Python Basics',
            description='Learn Python',
            course_code='PY101'
        )
        
        with self.assertRaises(IntegrityError):
            Course.objects.create(
                title='Advanced Python',
                description='Advanced Python',
                course_code='PY101'
            )
    
    def test_course_audit_fields(self):
        """Test course audit fields are set"""
        course = Course.objects.create(
            title='Test Course',
            description='Test description',
            course_code='TEST101',
            created_by=self.teacher
        )
        
        self.assertIsNotNone(course.created_at)
        self.assertEqual(course.created_by, self.teacher)
    
    def test_course_with_modules(self):
        """Test course can have modules through intermediate table"""
        course = Course.objects.create(
            title='Python Course',
            description='Learn Python',
            course_code='PYTHON'
        )
        
        module1 = Module.objects.create(
            name='Module 1',
            module_code='M1',
            complexity='beginner'
        )
        module2 = Module.objects.create(
            name='Module 2',
            module_code='M2',
            complexity='intermediate'
        )
        
        CourseModuleOrder.objects.create(course=course, module=module1, order=1)
        CourseModuleOrder.objects.create(course=course, module=module2, order=2)
        
        self.assertEqual(course.modules.count(), 2)
        self.assertEqual(list(course.modules.all())[0], module1)


class ModuleModelTestCase(APITestCase):
    """Test cases for Module model"""
    
    def test_module_creation(self):
        """Test module creation"""
        module = Module.objects.create(
            name='Introduction to Python',
            module_code='INTRO-PY',
            topics_list='Variables, Loops, Functions',
            complexity='beginner'
        )
        
        self.assertIsNotNone(module)
        self.assertEqual(module.name, 'Introduction to Python')
        self.assertEqual(module.complexity, 'beginner')
    
    def test_module_str_representation(self):
        """Test module string representation"""
        module = Module.objects.create(
            name='Test Module',
            module_code='TEST-MOD'
        )
        
        self.assertEqual(str(module), 'Test Module')
    
    def test_module_complexity_choices(self):
        """Test module complexity field choices"""
        for complexity in ['beginner', 'intermediate', 'expert']:
            module = Module.objects.create(
                name=f'Test Module {complexity}',
                module_code=f'TEST-{complexity[:3].upper()}',
                complexity=complexity
            )
            self.assertEqual(module.complexity, complexity)
    
    def test_module_with_lessons(self):
        """Test module can have lessons through intermediate table"""
        module = Module.objects.create(
            name='Test Module',
            module_code='TEST-MOD'
        )
        
        lesson1 = Lesson.objects.create(
            lesson_name='Lesson 1',
            lesson_code='L1'
        )
        lesson2 = Lesson.objects.create(
            lesson_name='Lesson 2',
            lesson_code='L2'
        )
        
        ModuleLessonOrder.objects.create(module=module, lesson=lesson1, order=1)
        ModuleLessonOrder.objects.create(module=module, lesson=lesson2, order=2)
        
        self.assertEqual(module.lessons.count(), 2)


class LessonModelTestCase(APITestCase):
    """Test cases for Lesson model"""
    
    def test_lesson_creation(self):
        """Test lesson creation"""
        lesson = Lesson.objects.create(
            lesson_name='Hello World',
            lesson_code='HW001',
            topic_objective='Learn to print Hello World'
        )
        
        self.assertIsNotNone(lesson)
        self.assertEqual(lesson.lesson_name, 'Hello World')
        self.assertEqual(lesson.lesson_code, 'HW001')
    
    def test_lesson_str_representation(self):
        """Test lesson string representation"""
        lesson = Lesson.objects.create(
            lesson_name='Test Lesson',
            lesson_code='TL001'
        )
        
        self.assertEqual(str(lesson), 'TL001 - Test Lesson')
    
    def test_lesson_code_nullable(self):
        """Test lesson code can be auto-generated"""
        lesson = Lesson.objects.create(
            lesson_name='Lesson without code'
        )
        
        self.assertIsNotNone(lesson.lesson_code)


class BatchModelTestCase(APITestCase):
    """Test cases for Batch model"""
    
    def setUp(self):
        """Set up test data"""
        self.course = Course.objects.create(
            title='Python Course',
            description='Learn Python',
            course_code='PY'
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
    
    def test_batch_creation(self):
        """Test batch creation"""
        batch = Batch.objects.create(
            name='Batch A',
            teacher=self.teacher,
            batch_type='paid'
        )
        
        self.assertIsNotNone(batch)
        self.assertEqual(batch.name, 'Batch A')
        self.assertEqual(batch.batch_type, 'paid')
    
    def test_batch_str_representation(self):
        """Test batch string representation"""
        batch = Batch.objects.create(
            name='Test Batch',
            teacher=self.teacher
        )
        
        self.assertEqual(str(batch), 'Test Batch')
    
    def test_batch_students_relationship(self):
        """Test batch can have multiple students"""
        batch = Batch.objects.create(
            name='Test Batch',
            teacher=self.teacher,
            batch_type='paid'
        )
        
        student1 = Student.objects.create(
            user=User.objects.create_user(
                username='student1',
                email='student1@test.com',
                password='Test123!',
                user_type='student'
            ),
            school_name='School 1',
            student_grade='5'
        )
        student2 = Student.objects.create(
            user=User.objects.create_user(
                username='student2',
                email='student2@test.com',
                password='Test123!',
                user_type='student'
            ),
            school_name='School 2',
            student_grade='6'
        )
        
        batch.students.add(student1)
        batch.students.add(student2)
        
        self.assertEqual(batch.students.count(), 2)


class EnrollmentModelTestCase(APITestCase):
    """Test cases for Enrollment model"""
    
    def setUp(self):
        """Set up test data"""
        self.course = Course.objects.create(
            title='Python Course',
            description='Learn Python',
            course_code='PY'
        )
        self.user = User.objects.create_user(
            username='student',
            email='student@test.com',
            password='TestPass123!',
            user_type='student',
            name='Test Student'
        )
        self.student = Student.objects.create(
            user=self.user,
            school_name='Test School',
            student_grade='5'
        )
    
    def test_enrollment_creation(self):
        """Test enrollment creation"""
        enrollment = Enrollment.objects.create(
            student=self.student,
            course='Python Course',
            service_type='Prime'
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
        
        enrollment_str = str(enrollment)
        self.assertIn('Enrollment', enrollment_str)
        self.assertIn(self.student.user.name, enrollment_str)
