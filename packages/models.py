from django.db import models

# Create your models here.
class Packages(models.Model):

    class Meta:
        verbose_name_plural = 'Packages'

    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name
