from django.db import models

# Create your models here.

class MainInformation(models.Model):
    title =  models.CharField(max_length=255)
    main = models.TextField(blank=True)
