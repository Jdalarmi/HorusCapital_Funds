# Generated by Django 5.0 on 2023-12-21 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_rename_juros_jurostable_value_month_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableFutureFees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_investido', models.FloatField()),
                ('juros', models.FloatField()),
                ('total_acumulado', models.FloatField()),
            ],
        ),
    ]
