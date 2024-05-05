from django.db import models

NULLABLE = {'blank':  True, 'null': True}


class Product(models.Model):
    """"
    Модель продукта
    """
    name = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(max_length=100, verbose_name='Модель', **NULLABLE)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата выхода на рынок')
    price = models.FloatField(verbose_name='Цена', **NULLABLE)

    def __str__(self):
        return f'{self.name} - {self.price} '

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Contact(models.Model):
    """"
    Модель контактов
    """
    email = models.EmailField(max_length=150, verbose_name='email')
    country = models.CharField(max_length=100, verbose_name='Страна', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    street = models.CharField(max_length=100, verbose_name='Улица', **NULLABLE)
    number = models.PositiveIntegerField(verbose_name='Номер дома', **NULLABLE)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Seller(models.Model):
    """"
    Модель торговой сети
    """
    SELLER_TYPES = [
        (0, 'Завод'),
        (1, 'Магазин'),
        (2, 'ИП')
    ]
    seller_type = models.PositiveIntegerField(choices=SELLER_TYPES, verbose_name='Тип')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE, verbose_name='Контакты')
    products = models.ManyToManyField('Product', verbose_name='Продукты')
    supplier = models.ForeignKey('Seller', on_delete=models.PROTECT, verbose_name='Поставщик', **NULLABLE)
    debt = models.FloatField(verbose_name='Задолженность перед поставщиком', **NULLABLE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'
