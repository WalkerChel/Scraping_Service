# Generated by Django 4.1.5 on 2023-02-02 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0003_vacancy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancy',
            options={'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
        migrations.AddField(
            model_name='vacancy',
            name='timestamptime',
            field=models.TimeField(auto_now=True),
        ),
    ]
