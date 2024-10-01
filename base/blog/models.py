from django.db import models
from django.contrib.auth.models import User


class Categori(models.Model):
    name=models.CharField(max_length=200, verbose_name="name")
    created=models.DateTimeField(auto_now_add=True, verbose_name="creada")
    updated=models.DateTimeField(auto_now=True, verbose_name="actualizada")



    class Meta:
        verbose_name="categori"
        verbose_name_plural="categoris"
        
    def __str__(self):
        return self.name
        
class Post(models.Model):
    title=models.CharField(max_length=200, verbose_name="titulo")
    content=models.TextField(max_length=200, verbose_name="contenido")
    image=models.ImageField(upload_to='blog', verbose_name="imagen", null=True, blank=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    categori=models.ManyToManyField(Categori)
    created=models.DateTimeField(auto_now_add=True, verbose_name="creada")
    updated=models.DateTimeField(auto_now=True, verbose_name="actualizada")



    class Meta:
        verbose_name="post"
        verbose_name_plural="posts"
        
    def __str__(self):
        return self.title