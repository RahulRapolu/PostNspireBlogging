# Generated by Django 3.2.4 on 2021-06-27 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blogpost_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_posted',
            field=models.DateTimeField(),
        ),
    ]