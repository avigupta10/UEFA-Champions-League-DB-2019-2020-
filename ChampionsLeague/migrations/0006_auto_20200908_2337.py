# Generated by Django 3.1.1 on 2020-09-08 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ChampionsLeague', '0005_auto_20200908_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='Club_Manager',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manager', to='ChampionsLeague.manager'),
        ),
    ]