from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful """
        email = 'teeruch.k@gmail.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        """ เช็คว่าสร้าง user ได้มั้ย โดยเอา email ไป test ใน function 
        get_user_model  ลอง test จะ fail เพราะ create_user
        ต้องการ username field ด้วย กรณีนี้เราจะ modify custom user"""

        self.assertEqual(user.email, email)
        """ return email กลับมา """
        self.assertTrue(user.check_password(password))
        """ เช็คว่า True หรือ false โดยใช้ method check_password """

    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized """
        """ ตั้งค่าให้ email ที่ input เข้ามา ถูก django เก็บเป็นตัวพิมพ์เล็ก """
        email = 'test@GMAIL.COM'

        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())
        """ test normalized เช็ค email ที่ test ทำเป็นตัวพิมพ์เล็ก ต้องเท่ากับ return email ที่มาจาก models """

    def test_new_user_invalid_email(self):
        """ เช็คว่าเป้น email หรือไม่ โดยให้ models แสดง error """
        """ Test creating user with no email raise error """

        with self.assertRaises(ValueError):
            """ เช็คว่ามี raise Value error ขึ้นมั้ย ถ้ากรอกผิด """
            get_user_model().objects.create_user(None, 'Pass1234')

    def test_create_new_superuser(self):
        """
        test create super user in command line
        super user จะเป็น is_staff = True, is_superuser = True
        """
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
