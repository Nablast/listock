# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-25 19:55
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nom')),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantityInList', models.IntegerField(blank=True, default=0, verbose_name='Quantite')),
                ('quantityInStock', models.IntegerField(blank=True, default=0, verbose_name='Quantite')),
                ('unity', models.CharField(choices=[('weight', 'Weight'), ('liquid', 'Liquid'), ('number', 'Number'), ('pack', 'Pack'), ('None', 'None')], default='None', max_length=255)),
                ('entryDateInStock', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Listock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('lastmaj_date', models.DateField(auto_now=True)),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='listock', to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nom')),
                ('description', models.CharField(max_length=255, verbose_name='Nom')),
                ('expiryAverageTime', models.DurationField(blank=True, default=datetime.timedelta)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objectsInside', to='listock.Category')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='listock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='listock.Listock'),
        ),
        migrations.AddField(
            model_name='item',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='listock.Object'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='listock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='listock.Listock'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='userFrom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitationsSent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invitation',
            name='userTo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to=settings.AUTH_USER_MODEL),
        ),
    ]
