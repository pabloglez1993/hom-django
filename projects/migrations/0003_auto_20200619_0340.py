# Generated by Django 3.0.7 on 2020-06-19 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200619_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(blank=True, choices=[('Department', 'Department'), ('House', 'House'), ('Building', 'Building'), ('Reparation', 'Reparation'), ('Other', 'Other')], max_length=10, null=True),
        ),
    ]
