# Generated by Django 3.0.8 on 2020-07-04 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_personalnote'),
    ]

    operations = [
        migrations.CreateModel(
            name='EEG_Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=200)),
                ('num_channels', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
            ],
        ),
    ]
