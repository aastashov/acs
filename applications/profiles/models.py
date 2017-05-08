# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from applications.infrastructure.models import Departament, Position


# Create your models here.
GENDER_CHOICES = (
    ('М', 'Мужской'),
    ('F', 'Женский'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь')
    first_name = models.CharField(max_length=15, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    position = models.ForeignKey(Position, verbose_name='Должность')
    gender = models.CharField(max_length=2, verbose_name='Пол', choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    home_phone = models.CharField(max_length=15, verbose_name='Домашний телефон', blank=True, null=False)
    address = models.CharField(max_length=50, verbose_name='Адрес')
    image = models.ImageField(blank=True, null=True, verbose_name='Фотография')
    birthday = models.DateField(verbose_name='Дата рождения')
    active = models.BooleanField(verbose_name='Активен', default=False)

    def __unicode__(self):
        return '{} {}'.format(self.last_name, self.first_name)


class WorkPeriod(models.Model):
    employed = models.DateField(verbose_name='Принят на работу с ', blank=True, null=True)
    dismissed = models.DateField(verbose_name='Уволен с ', blank=True, null=True)
    reason_for_leaving = models.TextField(blank=True, null=True, verbose_name='Причина увольнения')
