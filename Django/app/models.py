from django.db import models


class Wish(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    cost = models.DecimalField()
    image = models.ImageField(upload_to='images', null=True, blank=True)
