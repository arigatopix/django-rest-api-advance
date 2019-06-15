from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager,
                                        PermissionsMixin)


class UserManager(BaseUserManager):
    """
    helper function จะ overwrite function เดิมในการ /
    custom create_user กับ superuser
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        create and saves a new user
        **extra_fields คือถ้ามี field อื่นๆ เพิ่มขึ้นมา ไม่ต้องประกาศอีก
        """

        if not email:
            """เข็ค email ที่เข้ามา ถ้าไม่ใช่ email format ให้ขึ้นเตือน ValueError
            แล้วเราลองไป test
            ปกติจะสร้างไม่ผ่านอยู่แล้ว แต่ตรงนี้ให้ django แสดง message 
            และบอกว่าเกิด error ชนิดไหน"""
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        """ 
        เนื่องจากปกติ email ส่วนมากเป็น case insensitive
        แปลง email ที่ input เข้ามาเป็นตัวพิมพ์เล็กทั้งหมด 
        เวลา save ใน db จะได้ระบุว่า user ซ้ำหรือไม่
        """
        user = self.model(email=email, **extra_fields)
        """ กำหนดให้ user คือ email """
        user.set_password(password)
        """ set password input plain text แล้ว save เป็น hash """
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """
        Create and save a new super user
        ใช้ function จากด้านบน แล้วเปลี่ยน attribute นิดหน่อย
        """

        user = self.create_user(email, password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
        Custom user model that support using email instead of username
        สามารถกำหนด USERNAME_FIELD เป็นอย่างอื่นได้
        https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#django.contrib.auth.models.AbstractBaseUser
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    """ เรียก UserManager เอา email ไปใช้สร้าง user """
    """ User.objects.... เวลาเรียกไปใช้งาน """

    USERNAME_FIELD = 'email'
