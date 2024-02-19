# Generated by Django 5.0.2 on 2024-02-16 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0004_remove_xodim_bulim_bulim_xodim'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xodim',
            name='ish_turi',
        ),
        migrations.AddField(
            model_name='xodim',
            name='ish_turi',
            field=models.ManyToManyField(related_name='xodim_ish_turi', to='Post.ish_turi'),
        ),
    ]