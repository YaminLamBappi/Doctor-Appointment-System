from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField(blank=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
