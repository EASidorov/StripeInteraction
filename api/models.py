from django.db import models
from django.core.validators import RegexValidator


class Item(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)

    name = models.CharField(
        max_length=15,
        unique=True,
        verbose_name='Товар'
    )

    description = models.CharField(
        max_length=100,
        verbose_name='Описание'
    )


    price = models.PositiveIntegerField(
        verbose_name='Цена'
    )

    CURRENCY = (
        ("RUB", 'RUB'),
        ("USD", 'USD'),
    )
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY,
        default="RUB",
    )

    def __str__(self):
        return f'{self.name}, {self.price}, {self.description}'


class Discount(models.Model):
    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'
    discount_validator = RegexValidator(regex='^0*(100\.00|[0-9]?[0-9]\.[0-9]{2})%$',
                                        message='проверка процентов скидки')
    discount_rate = models.CharField(default='0',
                                     max_length=5,
                                     verbose_name='Размер скидки',
                                     validators=[discount_validator]
                                     )


class Tax(models.Model):
    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Налоги'

    tax_validator = RegexValidator(regex='^0*(100\.00|[0-9]?[0-9]\.[0-9]{2})%$',
                                        message='проверка процентов налога')
    tax_rate = models.CharField(default='0',
                                max_length=5,
                                verbose_name='Размер налога',
                                validators=[tax_validator]
                                )


class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    items = models.ManyToManyField(Item)
    DISCOUNTS = (
        ('0%', '0%'),
        ('5%', '5%'),
        ('10%', '10%'),
        ('25%', '25%'),
    )
    discounts = models.CharField(
        max_length=3,
        choices=DISCOUNTS,
        default='0%',
    )
    TAXES = (
        ('0%', '0%'),
        ('18%', '18%'),
        ('20%', '20%'),
        ('32%', '32%'),
    )
    taxes = models.CharField(
        max_length=3,
        choices=TAXES,
        default='0%',
    )

    def __str__(self):
        return f'{self.id}'
