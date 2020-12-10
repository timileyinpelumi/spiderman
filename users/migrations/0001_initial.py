# Generated by Django 3.1.3 on 2020-12-10 02:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('fname', models.CharField(max_length=25, verbose_name='firstname')),
                ('lname', models.CharField(max_length=25, verbose_name='lastname')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('password', models.CharField(max_length=25)),
                ('wallet_address', models.CharField(max_length=512, null=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]