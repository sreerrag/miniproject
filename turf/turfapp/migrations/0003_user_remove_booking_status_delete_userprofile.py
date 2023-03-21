# Generated by Django 4.1.7 on 2023-02-27 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turfapp', '0002_remove_turf_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='booking',
            name='status',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
