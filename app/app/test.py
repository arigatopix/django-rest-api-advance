# จะ run test  ได้เมื่อตั้งชื่อ file หรือ function ที่ตั้งชื่อว่า test นำหน้า
from django.test import TestCase

from app.calc import add, subtract


class CalTests(TestCase):

    def test_add_numbers(self):
        """ Test that two numbers are added together """
        self.assertEqual(add(3, 8), 11)
        """ function add ต้องเท่ากับ 11 """

    def test_subtract_numbers(self):
        """ เพิ่ม case อย่าลืมใส่ test_ นำหน้า function ถ้ามี fail จะมีรายละเอียดบอก"""
        """ docker-compose run app sh -c "python manage.py test" """
        self.assertEqual(subtract(2, 9), 7)
