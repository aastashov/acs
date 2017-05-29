# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 04:28
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('infrastructure', '0001_initial'),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this administrate has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A administrate with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the administrate can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this administrate should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(choices=[('\u041c', '\u041c\u0443\u0436\u0441\u043a\u043e\u0439'), ('F', '\u0416\u0435\u043d\u0441\u043a\u0438\u0439')], max_length=2, verbose_name='\u041f\u043e\u043b')),
                ('phone', models.CharField(max_length=15, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('home_phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='\u0414\u043e\u043c\u0430\u0448\u043d\u0438\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('address', models.CharField(max_length=50, verbose_name='\u0410\u0434\u0440\u0435\u0441')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/photo', verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f')),
                ('birthday', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this administrate belongs to. A administrate will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='administrate', to='auth.Group', verbose_name='groups')),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='infrastructure.Position', verbose_name='\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this administrate.', related_name='user_set', related_query_name='administrate', to='auth.Permission', verbose_name='administrate permissions')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0444\u0430\u0439\u043b',
                'verbose_name_plural': '\u041f\u0440\u043e\u0444\u0430\u0439\u043b\u044b',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='WorkPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employed', models.DateField(blank=True, null=True, verbose_name='\u041f\u0440\u0438\u043d\u044f\u0442 \u043d\u0430 \u0440\u0430\u0431\u043e\u0442\u0443 \u0441 ')),
                ('dismissed', models.DateField(blank=True, null=True, verbose_name='\u0423\u0432\u043e\u043b\u0435\u043d \u0441 ')),
                ('reason_for_leaving', models.TextField(blank=True, null=True, verbose_name='\u041f\u0440\u0438\u0447\u0438\u043d\u0430 \u0443\u0432\u043e\u043b\u044c\u043d\u0435\u043d\u0438\u044f')),
                ('administrate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u043f\u0435\u0440\u0438\u043e\u0434',
                'verbose_name_plural': '\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u043f\u0435\u0440\u0438\u043e\u0434',
            },
        ),
    ]
