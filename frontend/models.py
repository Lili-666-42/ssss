from django.db import models
from users.models import CustomUser 

class Contactt(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,  null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.image.name  # Используем имя файла изображения

