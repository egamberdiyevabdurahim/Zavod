# Generated by Django 5.0.2 on 2024-03-06 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('Direktor', 'Direktor'), ('Admin', 'Admin'), ('Tekshiruvchi', 'Tekshiruvchi'), ('Bulum', 'Bulum')], default='Tekshiruvchi', max_length=12),
        ),
    ]
