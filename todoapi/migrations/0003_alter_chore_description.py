# Generated by Django 3.2.5 on 2021-07-26 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0002_alter_chore_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chore',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
