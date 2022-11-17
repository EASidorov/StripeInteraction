# Generated by Django 4.1.2 on 2022-11-17 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_item_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='discounts',
            field=models.CharField(choices=[('0%', '0%'), ('5%', '5%'), ('10%', '10%'), ('25%', '25%')], default='0%', max_length=3),
        ),
        migrations.AlterField(
            model_name='order',
            name='taxes',
            field=models.CharField(choices=[('0%', '0%'), ('18%', '18%'), ('20%', '20%'), ('32%', '32%')], default='0%', max_length=3),
        ),
    ]
