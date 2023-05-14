from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class Item(models.Model):
    video = EmbedVideoField()

class Products(models.Model):
    name = models.CharField(max_length=220, null=True)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(null=True, blank=False)

    def __str__ (self):
        return self.name

    @property
    def imageURL(self):
        try:
            url= self.image.url
        except:
            url = ''
        return url