# Generated by Django 4.1.2 on 2023-06-05 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_newsdata_user_id_alter_newsdata_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsdata',
            name='content',
            field=models.TextField(max_length=1000),
        ),
    ]
