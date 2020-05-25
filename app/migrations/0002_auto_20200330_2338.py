# Generated by Django 3.0.3 on 2020-03-30 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appsuccess',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='appsuccess',
            name='ContentRating',
        ),
        migrations.AlterField(
            model_name='appsuccess',
            name='Price',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='appsuccess',
            name='Rating',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='appsuccess',
            name='Reviews',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='appsuccess',
            name='Size',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='appsuccess',
            name='Type',
            field=models.CharField(max_length=250),
        ),
    ]
