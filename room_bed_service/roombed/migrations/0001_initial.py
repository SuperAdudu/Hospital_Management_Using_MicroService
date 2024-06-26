# Generated by Django 4.1.13 on 2024-05-30 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.CharField(max_length=10)),
                ('note', models.CharField(max_length=500)),
                ('type', models.CharField(max_length=10)),
                ('buildingName', models.CharField(max_length=10)),
                ('roomNumber', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=500)),
                ('price', models.CharField(max_length=100)),
                ('bedNumber', models.CharField(max_length=1000)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roombed.room')),
            ],
        ),
    ]
