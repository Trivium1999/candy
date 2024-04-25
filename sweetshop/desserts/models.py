from django.db import models
from django.shortcuts import reverse


class ExampleDecoration(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/decorations/example/', null=True)
    examples = models.ManyToManyField('Decorations', blank=True, related_name='decorations')
    # slug = models.SlugField(max_lenght=150, unique=True)

    class Meta:
        verbose_name = 'Десерт'
        verbose_name_plural = 'Десерты'
        ordering = ["-id"]

    def get_absolute_url(self):
        return reverse('desserts:example', kwargs={'id': self.id})

    def __str__(self):
        return '{}'.format(self.id)


class Decorations(models.Model):
    title = models.CharField(max_length=255, blank=False)
    image = models.ImageField(upload_to='image/decorations/', null=True)

    class Meta:
        verbose_name = 'Вид десерта'
        verbose_name_plural = 'Виды десертов'

    def __str__(self):
        return '{}'.format(self.title)


class ExampleFilling(models.Model):
    # image = models.ImageField(upload_to='image/fillings/example/', null=True)
    title = models.CharField(max_length=150)
    fillings = models.ManyToManyField('Fillings', blank=True, related_name='examples')
    # slug = models.SlugField(max_lenght=150, unique=True)

    class Meta:
        verbose_name = 'Начинка'
        verbose_name_plural = 'Начинки'        

    def get_absolute_url(self):
        return reverse('desserts:example', kwargs={'id': self.id})

    def __str__(self):
        return '{}'.format(self.title)


class Fillings(models.Model):
    title = models.CharField(max_length=255, blank=False)
    image = models.ImageField(upload_to='image/fillings/', null=True)
    description = models.TextField('Описание', blank=False)
    

    class Meta:
        verbose_name = 'Пример начинки'
        verbose_name_plural = 'Примеры начинок'

    # def get_absolute_url(self):
    #     return reverse('desserts:example', kwargs={'id': self.id})

    def __str__(self):
        return '{}'.format(self.title)
