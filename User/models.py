from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    STATUS = (
        ('Diretor', 'Diretor'),
        ('Admin', 'Admin'),
        ('Tekshiruvchi', 'Tekshiruvchi'),
        ('Bulum', 'Bulum'),
    )
    
    GENDER = (
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
        ('Null', 'Null'),
    )

    phone = models.CharField(max_length=14, null=True, blank=True)
    photo = models.ImageField(upload_to='user_photo/', default='base.jpg')
    gender = models.CharField(max_length=10, choices=GENDER, default='Null')
    status = models.CharField(max_length=12, choices=STATUS, default='Tekshiruvchi')

    def __str__(self):
        return f'{self.first_name}/{self.status}'
