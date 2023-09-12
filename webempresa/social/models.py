from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(max_length=100, verbose_name="Nombre clave", unique=True)
    name = models.CharField(verbose_name="Red social", max_length=200)
    url = models.URLField(verbose_name="url",  max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de modificación')

    class Meta:
        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'
        ordering = ["-name"] #El guión es para hacerlo descendente

    def __str__(self):
        return self.name