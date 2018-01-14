from django.db import models

# Create your models here.
class Tipo(models.Model):
    title = models.CharField(max_length=100, verbose_name='Nome')
    description = models.TextField(verbose_name='Descrição')

    def __str__(self):
        return self.title

class Servico(models.Model):
    numero = models.CharField(max_length=10, verbose_name='Número')
    tipo = models.ForeignKey(Tipo,verbose_name='Tipo')

    def __str__(self):
        return self.numero
