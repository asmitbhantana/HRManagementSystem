# Generated by Django 3.1.2 on 2020-10-30 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choose_answer',
            field=models.CharField(choices=[('1', 'Option 1'), ('2', 'Option 2'), ('3', 'Option 3'), ('4', 'Option 4')], max_length=1),
        ),
    ]
