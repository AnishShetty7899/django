# Generated by Django 5.0.4 on 2024-05-01 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoApps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=100)),
                ('points', models.IntegerField(default=1)),
                ('img', models.ImageField(upload_to='img')),
            ],
        ),
    ]
