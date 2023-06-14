# Generated by Django 4.1.2 on 2023-06-01 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=250)),
                ('image', models.FileField(upload_to='')),
                ('video', models.FileField(upload_to='')),
            ],
        ),
    ]
