# Generated by Django 3.2 on 2021-04-28 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_auto_20210428_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('student', 'st'), ('teacher', 'th')], max_length=50, verbose_name='type'),
        ),
    ]
