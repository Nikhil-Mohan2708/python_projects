from django.db import models

# Create your models here.
class remainder(models.Model):
    name=models.CharField(max_length=150)
    priority=models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return self.name
