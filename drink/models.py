from django.db import models

# Create your models here.

class Drink(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=240, blank=False, null=False)

    def __str__(self):
        return self.name

    