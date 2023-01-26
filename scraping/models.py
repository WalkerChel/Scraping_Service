from django.db import models

class city (models.Model):
    name = models.CharField(max_length=50, verbose_name='Название населённого пункта')
    slug = models.CharField(max_length=50, blank=True)
    
    class Meta:
        verbose_name = 'Название населённого пункта'
        verbose_name_plural = 'Название населённых пунктов'

    def __str__(self):
        return self.name
