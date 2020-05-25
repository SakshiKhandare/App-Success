# Generated by Django 3.0.3 on 2020-03-30 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200330_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='appsuccess',
            name='Category',
            field=models.CharField(choices=[('family', 'FAMILY'), ('game', 'GAME'), ('tools', 'TOOLS'), ('medical', 'MEDICAL'), ('business', 'BUSINESS'), ('productivity', 'PRODUCTIVITY'), ('personalization', 'PERSONALIZATION'), ('communication', 'COMMUNICATION'), ('sports', 'SPORTS'), ('lifestyle', 'LIFESTYLE')], default='kuch', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appsuccess',
            name='ContentRating',
            field=models.CharField(choices=[('everyone', 'Everyone'), ('teen', 'Teen'), ('everyone 10+', 'Everyone 10+'), ('mature 17+', 'Mature 17+'), ('adults only 18+', 'Adults only 18+'), ('unrated', 'Unrated')], default='r', max_length=20),
            preserve_default=False,
        ),
    ]
