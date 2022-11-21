from django.db import models


class Contact(models.Model):
    """
    A Contact model for customers submit enqueries
    """

    full_name = models.CharField(max_length=80, null=False, blank=False)
    email_address = models.EmailField(max_length=80, null=False, blank=False)
    message = models.TextField(max_length=5000, null=False, blank=False)

    def __str__(self):
        return self.full_name
