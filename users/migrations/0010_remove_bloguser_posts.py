# Generated by Django 4.1.3 on 2022-11-09 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_bloguser_posts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloguser',
            name='posts',
        ),
    ]