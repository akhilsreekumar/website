from django.db import models

# Create your models here.

class Temper(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.value

    class Meta:
        ordering = ('created',)