# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-11 10:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='教师名字')),
                ('work_years', models.IntegerField(default=0, verbose_name='工作年限')),
                ('work_company', models.CharField(max_length=50, verbose_name='就职公司')),
                ('work_position', models.CharField(max_length=50, verbose_name='公司职位')),
                ('points', models.CharField(max_length=50, verbose_name='教学特点')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏数')),
                ('age', models.IntegerField(default=30, verbose_name='年龄')),
                ('image', models.ImageField(default='', upload_to='teacher/%Y/%m', verbose_name='头像')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '教师',
                'verbose_name_plural': '教师',
            },
        ),
    ]
