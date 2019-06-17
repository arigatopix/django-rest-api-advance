from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        """ สร้าง instance เอาไว้สำหรับ test """
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@gmail.com',
            password='1234'
        )
        self.client.force_login(self.admin_user)
        """ ช่วยในการ login ผ่าน auth ของ django """

        self.user = get_user_model().objects.create_user(
            email='test@gmail.com',
            password='1234',
            name='Test Full name'
        )

    def test_user_listed(self):
        """ list user ใน user page admin """
        url = reverse('admin:core_user_changelist')
        """ 
        generate url list page ดูใน doc อีกที 
        https://docs.djangoproject.com/en/2.1/ref/contrib/admin/
        """

        response = self.client.get(url)
        """ รับ list user มา """

        self.assertContains(response, self.user.name)
        """ เช็คว่า user ที่สร้างใน setUp ออกมามั้ย """
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        """ test that the user edit page work หน้า admin edit user"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        """ admin/core/user/id กรณีเปลี่ยนหน้า login ?? """
        """ https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets """

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        """ เช็คว่า request ผ่านมั้ย ตอบ status code 200 """

    def test_create_user_page(self):
        """ Test that create user page work """

        """ เช็ค function admin หน้าเพิ่ม user """
        url = reverse('admin:core_user_add')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
