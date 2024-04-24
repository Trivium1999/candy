from django.db import models


class Filling(models.Model):
    """Начинки для десертов. От этой модели наследуются все остальные 'начинки'."""
    name = models.CharField('Название начинки', blank=False, max_length=100)
    description = models.TextField('Описание начинки', blank=False)

    class Meta:
        abstract = True


class CakeFilling(Filling):
    """Начинки для тортов."""
    price = models.IntegerField('Наценка')
    image = models.ImageField(upload_to='image/filling/cake/', null=True, blank=False)

    class Meta:
        verbose_name = 'Начинка для торта'
        verbose_name_plural = 'Начинки для тортов'

    def __str__(self):
        return f'{self.name}'


class CupcakeFilling(Filling):
    """Начинки для капкейков."""

    class Meta:
        verbose_name = 'Начинка для капкейков'
        verbose_name_plural = 'Начинки для капкейков'

    def __str__(self):
        return f'{self.name}'


class BentoFilling(Filling):
    """Начинки для бенто-тортов."""
    image = models.ImageField(upload_to='image/filling/bento/', null=True, blank=False)

    class Meta:
        verbose_name = 'Начинка для бенто-торта'
        verbose_name_plural = 'Начинки для бенто-тортов'

    def __str__(self):
        return f'{self.name}'


class Decoration(models.Model):
    """Оформление десертов. От этой модели наследуются все остальные с 'оформлением'."""
    name = models.CharField('Тип оформления', max_length=100)
    description = models.TextField('Описание оформления')
    price = models.IntegerField('Наценка')

    class Meta:
        abstract = True


class CakeDecoration(Decoration):
    """Виды оформления тортов."""

    class Meta:
        verbose_name = 'Оформление тортов'
        verbose_name_plural = 'Оформление тортов'

    def __str__(self):
        return f'{self.name}'


class CupcakeDecoration(Decoration):
    """Виды оформления капкейков."""

    class Meta:
        verbose_name = 'Оформление капкейков'
        verbose_name_plural = 'Оформление капкейков'

    def __str__(self):
        return f'{self.name}'


class Desserts(models.Model):
    date = models.CharField(
        'На какое число хотите заказать?',
        max_length=100,
        blank=False
    )
    description = models.TextField('Описание', blank=False)
    price = models.IntegerField('Цена')
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        abstract = True


class Cake(Desserts):
    filling = models.OneToOneField(
        CakeFilling,
        on_delete=models.CASCADE,
        verbose_name='Начинка'
    )
    decoration = models.OneToOneField(
        CakeDecoration,
        on_delete=models.CASCADE,
        verbose_name='Оформление'
    )

    class Meta:
        verbose_name = 'Торт'
        verbose_name_plural = 'Торты'

    def __str__(self):
        return f'{self.date}'


class Cupcake(Desserts):
    filling = models.OneToOneField(
        CupcakeFilling,
        verbose_name='Начинка',
        on_delete=models.CASCADE
    )
    decoration = models.OneToOneField(
        CupcakeDecoration,
        verbose_name='Оформление',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Капкейки'
        verbose_name_plural = 'Капкейки'

    def __str__(self):
        return f'{self.date}'


class BentoCake(Desserts):
    filling = models.OneToOneField(
        BentoFilling,
        verbose_name='Начинка',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Бенто-торт'
        verbose_name_plural = 'Бенто-торты'

    def __str__(self):
        return f'{self.date}'


class OtherDessert(Desserts):
    name = models.CharField('Тип десерта', max_length=100)

    class Meta:
        verbose_name = 'Десерт'
        verbose_name_plural = 'Разные Десерты'

    def __str__(self):
        return f'{self.date}'
