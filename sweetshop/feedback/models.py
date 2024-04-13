from django.db import models


class Reviews(models.Model):
    description = models.TextField('Описание', blank=True)
    image = models.ImageField(upload_to="users/%Y/%m/",
                              blank=True, null=True,
                              verbose_name="Фото отзыва")
