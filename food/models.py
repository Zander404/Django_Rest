from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=400, null=False, blank=False)
    
    def __str__(self):
        return self.name