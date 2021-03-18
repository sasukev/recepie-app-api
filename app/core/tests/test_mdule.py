from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_success(self):
        """test creating new user with email is successful"""
        email = "test@pythonemail.com"
        password = "test_123"

        user = get_user_model().objects.create_user(emil=email , password=password)

        self.assertEqual(user.email == email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        """test the email for the new user is normalized """

        email = "test@PYTHONEMAIL.com"
        user = get_user_model().objects.create_user(email,'test123')

        self.assertEqual(user.email, email.lower())
