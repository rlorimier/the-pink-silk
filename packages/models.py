from django.db import models


class Packages(models.Model):
    """ Creates a packages model """

    class Meta:
        verbose_name_plural = 'Packages'

    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.TextField()
    description = models.TextField()
    included1 = models.TextField(null=True, blank=True)
    included2 = models.TextField(null=True, blank=True)
    included3 = models.TextField(null=True, blank=True)
    treatments1 = models.TextField(null=True, blank=True)
    treatments2 = models.TextField(null=True, blank=True)
    treatments3 = models.TextField(null=True, blank=True)
    treatments4 = models.TextField(null=True, blank=True)
    treatments5 = models.TextField(null=True, blank=True)
    treatments6 = models.TextField(null=True, blank=True)
    treatments7 = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
