# Generated by Django 4.2.4 on 2023-09-16 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0004_alter_district_state_fk_alter_user_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=256, unique=True, verbose_name='Business Name')),
                ('business_type', models.PositiveSmallIntegerField(choices=[(1, 'Hall Renter'), (2, 'Catress')], verbose_name='Business Type')),
                ('business_address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Business Address')),
                ('contect_no', models.CharField(max_length=13, verbose_name='Contect Number')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.country', verbose_name='Country FK')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.district', verbose_name='District FK')),
                ('states', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.state', verbose_name='State FK')),
                ('user_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hall_renter', to=settings.AUTH_USER_MODEL, verbose_name='Vender')),
            ],
        ),
        migrations.CreateModel(
            name='Catress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catress_name', models.CharField(max_length=200, verbose_name='Catress Name')),
                ('capacity', models.IntegerField(verbose_name='People capacity')),
                ('address', models.CharField(max_length=200, verbose_name='Catress Address')),
                ('total_price', models.IntegerField(blank=True, null=True, verbose_name='Price')),
                ('package_preference', models.PositiveSmallIntegerField(choices=[(1, 'Elite Package'), (2, 'Prime Package'), (3, 'Budget Package')], verbose_name='Package Preference')),
                ('area', models.CharField(max_length=100, verbose_name='Area')),
                ('contect_no', models.CharField(max_length=13, unique=True, verbose_name='Contect Number')),
                ('is_contect_no_verified', models.BooleanField(default=False, verbose_name='Is Contect No Active')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('business_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.business', verbose_name='Business')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.country', verbose_name='Country FK')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.district', verbose_name='District FK')),
                ('states', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.state', verbose_name='State FK')),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_name', models.CharField(max_length=200, verbose_name='Hall Name')),
                ('capacity', models.IntegerField(verbose_name='Hall capacity')),
                ('rooms', models.IntegerField(verbose_name='Room Count')),
                ('address', models.CharField(max_length=200, verbose_name='Hall Address')),
                ('price_par_wedding', models.FloatField(verbose_name='Price Par Wedding')),
                ('package_preference', models.PositiveSmallIntegerField(choices=[(1, 'Elite Package'), (2, 'Prime Package'), (3, 'Budget Package')], verbose_name='Package Preference')),
                ('area', models.CharField(max_length=100, verbose_name='Area')),
                ('contect_no', models.CharField(max_length=13, unique=True, verbose_name='Contect Number')),
                ('is_contect_no_verified', models.BooleanField(default=False, verbose_name='Is Contect No Active')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('business_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.business', verbose_name='Business')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.country', verbose_name='Country FK')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.district', verbose_name='District FK')),
                ('states', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.state', verbose_name='State FK')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_price', models.FloatField(blank=True, null=True, verbose_name='Package Price')),
                ('package_type', models.PositiveSmallIntegerField(choices=[(1, 'Elite Package'), (2, 'Prime Package'), (3, 'Budget Package')], verbose_name='Package Type')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('catress_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Catress', to='package.catress', verbose_name='Catress')),
                ('hall_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Hall', to='package.hall', verbose_name='Hall')),
            ],
        ),
    ]
