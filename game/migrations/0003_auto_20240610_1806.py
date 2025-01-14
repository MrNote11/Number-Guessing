# Generated by Django 3.2.25 on 2024-06-10 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='achievements',
            field=models.ManyToManyField(blank=True, to='game.Achievement'),
        ),
    ]
