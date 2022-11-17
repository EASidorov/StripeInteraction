# Generated by Django 4.1.2 on 2022-11-17 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_discount_options_alter_tax_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('rub', 'RUB'), ('usd', 'USD')], default='rub', max_length=3),
        ),
    ]