# Generated by Django 5.0.6 on 2024-06-12 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=100)),
                ('eemail', models.EmailField(max_length=100)),
                ('epassword', models.CharField(max_length=100)),
            ],
        ),
    ]
