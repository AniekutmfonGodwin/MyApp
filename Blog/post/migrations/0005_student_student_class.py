# Generated by Django 3.2 on 2021-04-24 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20210424_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_class',
            field=models.ManyToManyField(to='post.Class'),
        ),
    ]
