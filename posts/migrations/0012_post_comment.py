# Generated by Django 4.1.3 on 2022-11-18 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.ManyToManyField(related_name='comments', to='posts.comment'),
        ),
    ]
