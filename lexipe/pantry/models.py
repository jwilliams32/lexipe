from django.db import models


# Create your models here.
class Pantry(models.Model):

    pantry_name = models.TextField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.pantry_name)
