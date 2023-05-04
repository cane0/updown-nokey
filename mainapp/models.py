from django.db import models
from django.contrib.auth.models import User

class UpImg(models.Model):
    name = models.CharField(max_length=50)
    up_img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
