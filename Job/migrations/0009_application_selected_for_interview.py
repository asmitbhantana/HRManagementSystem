# Generated by Django 3.1 on 2020-08-14 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0008_auto_20200814_0634'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='selected_for_interview',
            field=models.BooleanField(default=False),
        ),
    ]
