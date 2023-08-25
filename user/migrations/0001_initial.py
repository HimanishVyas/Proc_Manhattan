# Generated by Django 4.2.4 on 2023-08-21 17:22

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='Mobile Number')),
                ('password', models.CharField(max_length=200, verbose_name='Password')),
                ('user_image', models.ImageField(blank=True, default='media/user/user_318-159711.png', null=True, upload_to='media/user', verbose_name='User Image')),
                ('user_role', models.PositiveSmallIntegerField(choices=[(1, 'Customer'), (2, 'Vendor')], default=3, verbose_name='User Role')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff Status')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Superuser Status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('mobile_verify', models.BooleanField(default=False, verbose_name='Mobile Number Verify')),
                ('email_verify', models.BooleanField(default=False, verbose_name='Email Verify')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]