from django.db import models

# Create your models here.


class Facts(models.Model):
    fact = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.fact
    