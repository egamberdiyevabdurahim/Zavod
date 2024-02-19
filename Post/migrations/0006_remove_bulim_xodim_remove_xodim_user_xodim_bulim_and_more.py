# Generated by Django 5.0.2 on 2024-02-16 11:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0005_remove_xodim_ish_turi_xodim_ish_turi'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bulim',
            name='xodim',
        ),
        migrations.RemoveField(
            model_name='xodim',
            name='user',
        ),
        migrations.AddField(
            model_name='xodim',
            name='bulim',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='xodim_bulim', to='Post.bulim'),
        ),
        migrations.AlterField(
            model_name='bulim',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='missed',
            name='butun_soni',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='missed',
            name='izoh',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='missed',
            name='xato_soni',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='xodim',
            name='gender',
            field=models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol'), ('Null', 'Null')], default='Null', max_length=10),
        ),
        migrations.AlterField(
            model_name='xodim',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='xodim',
            name='photo',
            field=models.ImageField(default='base.jpg', upload_to='xodim_photo/'),
        ),
    ]
