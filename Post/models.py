from django.db import models

from User.models import User


class Photo(models.Model):
    photo = models.ImageField(upload_to='missed_photo/')


class Ish_Turi(models.Model):
    name = models.CharField(max_length=40, unique=True)
    ish_id = models.CharField(max_length=9, unique=True)

    def __str__(self):
        return f'{self.name}/{self.ish_id}'


class Bulim(models.Model):
    name = models.CharField(max_length=90, unique=True)
    bulim_id = models.CharField(max_length=9, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name}/{self.bulim_id}/{self.user}'


class Xodim(models.Model):
    GENDER = (
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
        ('Null', 'Null'),
    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=GENDER, default='Null')
    photo = models.ImageField(upload_to='xodim_photo/', default='base.jpg')
    phone = models.CharField(max_length=15, null=True, blank=True)
    ish_turi = models.ManyToManyField(Ish_Turi, related_name='xodim_ish_turi')
    id_raqam = models.CharField(max_length=9, unique=True)
    bulimi = models.ForeignKey(Bulim, on_delete=models.CASCADE, related_name='xodim_bulim')

    def __str__(self):
        return f'{self.id_raqam}/{self.first_name}'



class Mahsulot(models.Model):
    name = models.CharField(max_length=90, unique=True)
    mahsulot_id = models.CharField(max_length=9, unique=True)

    def __str__(self):
        return f'{self.name}/{self.mahsulot_id}'


class Xatolar(models.Model):
    name = models.CharField(max_length=90, unique=True)
    xato_id = models.CharField(max_length=9, unique=True)

    def __str__(self):
        return f'{self.name}/{self.xato_id}'




class Missed(models.Model):
    xodim = models.ForeignKey(Xodim, on_delete=models.CASCADE, related_name='missed_xodim')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='missed_user')
    xato = models.ForeignKey(Xatolar, on_delete=models.CASCADE, related_name='missed_xato')
    xato_soni = models.PositiveIntegerField(default=0)
    butun_soni = models.PositiveIntegerField(default=0)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE, related_name='missed_mahsulot')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ManyToManyField(Photo, related_name='missed_photo')
    izoh = models.TextField(null=True, blank=True)
    ish_vaqti = models.PositiveIntegerField(null=True)
    audio = models.FileField(upload_to='missed_audio/', blank=True, null=True)

    def __str__(self):
        return f'{self.xodim}/{self.user}/{self.mahsulot}'
