from django.db import models

# Create your models here.
class Tost(models.Model):
    text=models.TextField('Текст')
    avtor=models.CharField('Автор',max_length=50)
    def __str__(self):
        return self.avtor
