from django.db import models

# Create your models here.
class movie (models.Model):
    name=models.CharField(max_length=250)
    description=models.TextField()
    year=models.IntegerField()
    images=models.ImageField(upload_to='Photos')

    def __str__(self):
        return self.name