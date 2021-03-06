# Generated by Django 3.2.5 on 2021-07-26 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChoreDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapi.chore')),
            ],
        ),
        migrations.CreateModel(
            name='Weekday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10)),
                ('chore', models.ManyToManyField(related_name='chore', through='todoapi.ChoreDay', to='todoapi.Chore')),
            ],
        ),
        migrations.AddField(
            model_name='choreday',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapi.weekday'),
        ),
        migrations.AddField(
            model_name='chore',
            name='weekday',
            field=models.ManyToManyField(related_name='weekday', through='todoapi.ChoreDay', to='todoapi.Weekday'),
        ),
    ]
