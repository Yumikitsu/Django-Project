# Generated by Django 5.1.5 on 2025-02-04 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceries_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registereduser',
            name='profilePic',
            field=models.ImageField(default='default.jpeg', upload_to='profile_pics'),
        ),
    ]
