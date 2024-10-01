from django.db import models

# Create your models here.

class Service(models.Model):
    title=models.CharField(max_length=200, verbose_name="titulo")
    content=models.TextField(max_length=200, verbose_name="contenido")
    image=models.ImageField(upload_to='servicio', verbose_name="imagen")
    created=models.DateTimeField(auto_now_add=True, verbose_name="creada")
    updated=models.DateTimeField(auto_now=True, verbose_name="actualizada")



    class Meta:
        verbose_name="servicio"
        verbose_name_plural="servicios"
        
    def __str__(self):
        return self.title
        






