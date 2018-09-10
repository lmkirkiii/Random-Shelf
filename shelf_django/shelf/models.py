from django.db import models

class Treasure(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    img_url = models.TextField()

    def __str__(self):
        return self.name