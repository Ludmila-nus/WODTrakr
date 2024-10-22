# Generated by Django 5.1 on 2024-10-22 13:07

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreferences',
            name='dark_mode',
            field=models.BooleanField(default=False, verbose_name='Dark mode'),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('es', 'Spanish')], default='en', max_length=10, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='notifications_enabled',
            field=models.BooleanField(default=True, verbose_name='Notifications enabled'),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='time_zone',
            field=models.CharField(default='UTC', max_length=50, verbose_name='Time zone'),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='Birthdate'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Full name'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/', verbose_name='Profile image'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]