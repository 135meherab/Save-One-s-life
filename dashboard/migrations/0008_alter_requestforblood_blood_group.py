# Generated by Django 4.2.7 on 2024-01-18 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_useraccount_blood_group'),
        ('dashboard', '0007_donationhistory_donation_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestforblood',
            name='blood_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.userbloodgroup'),
        ),
    ]
