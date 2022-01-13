from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test new user is created successfully"""
        email = 'test@test.com'
        password = 'test123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email for new user is normalized"""
        email = 'test@TEST.com'

        user = get_user_model().objects.create_user(
            email, 'test123'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating new user with invalid error raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_super_user(self):
        """Test creating new super user"""

        email = 'test@test.com'
        password = 'test124'

        user = get_user_model().objects.create_superuser(
            email, password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)