"""
Payment Model Tests for Codinzy Backend
"""

import pytest
from decimal import Decimal
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

from api.models import User, Payment, DiscountCode, StudentBilling, CreditTransaction, Student, Course


class PaymentModelTestCase(APITestCase):
    def setUp(self):
        student_user = User.objects.create_user(
            username='student', email='student@test.com',
            password='TestPass123!', user_type='student'
        )
        self.student = Student.objects.create(
            user=student_user, school_name='Test School', student_grade='5'
        )
    
    def test_payment_creation(self):
        payment = Payment.objects.create(
            student=self.student, amount=100.00,
            status='pending', payment_method='credit_card', currency='USD'
        )
        self.assertIsNotNone(payment)
        self.assertEqual(payment.amount, Decimal('100.00'))
    
    def test_payment_status_choices(self):
        for status in ['pending', 'completed', 'failed', 'refunded']:
            payment = Payment.objects.create(
                student=self.student, amount=100.00, status=status
            )
            self.assertEqual(payment.status, status)
    
    def test_payment_method_choices(self):
        for method in ['credit_card', 'debit_card', 'bank_transfer']:
            payment = Payment.objects.create(
                student=self.student, amount=100.00, payment_method=method
            )
            self.assertEqual(payment.payment_method, method)
    
    def test_payment_str_representation(self):
        payment = Payment.objects.create(student=self.student, amount=100.00)
        self.assertIsNotNone(str(payment))
    
    def test_payment_collection_link(self):
        payment = Payment.objects.create(
            student=self.student, amount=150.00, description='Course fee',
            collection_link='https://pay.example.com/abc123'
        )
        self.assertIsNotNone(payment.collection_link)


class DiscountCodeTestCase(APITestCase):
    def test_discount_code_creation(self):
        discount = DiscountCode.objects.create(
            discount_code='SAVE10', discount_percentage=10.00
        )
        self.assertIsNotNone(discount)
        self.assertEqual(discount.discount_code, 'SAVE10')
    
    def test_discount_code_str(self):
        discount = DiscountCode.objects.create(
            discount_code='TEST', discount_percentage=5
        )
        self.assertIn('TEST', str(discount))
    
    def test_discount_code_is_active_default(self):
        discount = DiscountCode.objects.create(
            discount_code='ACTIVE', discount_percentage=5
        )
        self.assertTrue(discount.is_active)


class StudentBillingTestCase(APITestCase):
    def setUp(self):
        student_user = User.objects.create_user(
            username='billing_student', email='billing@test.com',
            password='TestPass123!', user_type='student'
        )
        self.student = Student.objects.create(
            user=student_user, school_name='Test School', student_grade='5'
        )
    
    def test_student_billing_creation(self):
        billing = StudentBilling.objects.create(
            student=self.student, service_type='prime', class_size=5,
            cpc=Decimal('25.00'), payment_option='monthly',
            next_collection_amount=Decimal('125.00')
        )
        self.assertIsNotNone(billing)
        self.assertEqual(billing.service_type, 'prime')
    
    def test_student_billing_str(self):
        billing = StudentBilling.objects.create(
            student=self.student, service_type='plus', class_size=3,
            cpc=Decimal('30.00'), payment_option='installment',
            next_collection_amount=Decimal('90.00')
        )
        billing_str = str(billing)
        self.assertIn('plus', billing_str)
        self.assertIn('30.00', billing_str)
    
    def test_student_billing_service_type_choices(self):
        """Test service type field choices"""
        billing1 = StudentBilling.objects.create(
            student=self.student, service_type='prime', class_size=5,
            cpc=Decimal('25.00'), payment_option='monthly',
            next_collection_amount=Decimal('125.00')
        )
        self.assertEqual(billing1.service_type, 'prime')
        
        billing2 = StudentBilling.objects.create(
            student=Student.objects.create(
                user=User.objects.create_user(
                    username='billing_student2', email='billing2@test.com',
                    password='TestPass123!', user_type='student'
                ),
                school_name='Test School 2', student_grade='6'
            ),
            service_type='plus', class_size=5,
            cpc=Decimal('25.00'), payment_option='monthly',
            next_collection_amount=Decimal('125.00')
        )
        self.assertEqual(billing2.service_type, 'plus')


class CreditTransactionTestCase(APITestCase):
    def setUp(self):
        student_user = User.objects.create_user(
            username='credit_user', email='credit@test.com',
            password='TestPass123!', user_type='student'
        )
        self.student = Student.objects.create(
            user=student_user, school_name='Test School', student_grade='5'
        )
    
    def test_credit_transaction_creation(self):
        transaction = CreditTransaction.objects.create(
            student=self.student, transaction_type='credit',
            amount=100, description='Test credit transaction'
        )
        self.assertIsNotNone(transaction)
        self.assertEqual(transaction.amount, 100)
    
    def test_credit_transaction_type_choices(self):
        for trans_type in ['credit', 'referral', 'gift', 'refund']:
            transaction = CreditTransaction.objects.create(
                student=self.student, transaction_type=trans_type,
                amount=50, description=f'Test {trans_type} transaction'
            )
            self.assertEqual(transaction.transaction_type, trans_type)
    
    def test_credit_transaction_str(self):
        transaction = CreditTransaction.objects.create(
            student=self.student, transaction_type='credit',
            amount=100, description='Test credit transaction'
        )
        self.assertIn('credit', str(transaction))
