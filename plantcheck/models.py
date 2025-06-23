from django.db import models

# Create your models here.


class PlantImage(models.Model):
    """docstring for ClassName."""

    def __str__(self):
        return f"image uploaded on {self.uploaded_at.strftime('')}"
