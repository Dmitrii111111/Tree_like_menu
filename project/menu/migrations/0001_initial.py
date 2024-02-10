# Generated by Django 5.0.1 on 2024-02-08 17:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TreeMenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('verbose_name', models.CharField(blank=True, max_length=255, verbose_name='Verbose name')),
            ],
            options={
                'verbose_name': 'Menu category',
                'verbose_name_plural': 'Menu categories',
            },
        ),
        migrations.CreateModel(
            name='TreeMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('path', models.CharField(blank=True, max_length=1000, verbose_name='Link')),
                ('parent', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='menu.treemenu', verbose_name='Parent element')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.treemenucategory')),
            ],
            options={
                'verbose_name': 'Menu item',
                'verbose_name_plural': 'Menu items',
            },
        ),
    ]