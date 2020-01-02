from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    descriptions = models.TextField(blank=True)

    def __str__(self):
        return self.title