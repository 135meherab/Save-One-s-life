# Generated by Django 4.2.7 on 2024-01-18 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_userbloodgroup_alter_useraccount_blood_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='blood_group',
            field=models.CharField(choices=[('O-', 'O-'), ('AB+', 'AB+'), ('B-', 'B-'), ('O+', 'O+'), ('B+', 'B+'), ('A-', 'A-'), ('A+', 'A+'), ('AB-', 'AB-')], max_length=25),
        ),
    ]
