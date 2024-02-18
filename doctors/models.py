from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    education = models.TextField()
    areas_of_expertise = models.TextField(default="")
    contact_info = models.CharField(max_length=100)
    email = models.EmailField(default="example@example.com")
    phone = models.CharField(max_length=20, default="000-000-0000")

    image_url = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)

    # Consider adding a separate Review model and a ForeignKey here
    # patient_reviews = models.ForeignKey('Review', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
