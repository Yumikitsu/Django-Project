# Generated by Django 5.1.5 on 2025-02-04 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('wholelist', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
