# Generated by Django 4.2.5 on 2023-10-04 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SearchBase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='image',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Картинка'),
        ),
    ]
