# Generated by Django 2.2.10 on 2020-06-15 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200615_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('new', 'Interviews'), ('arts', 'Arts & Culture'), ('films', 'Film Reviews'), ('books', 'Book Reviews'), ('travel', 'Travel & Experience')], default='new', max_length=20),
        ),
    ]
