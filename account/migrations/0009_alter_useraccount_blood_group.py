# Generated by Django 4.2.7 on 2024-01-18 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_userbloodgroup_useraccount_blood_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='blood_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blood_group', to='account.userbloodgroup'),
        ),
    ]
