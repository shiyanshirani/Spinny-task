from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Box(models.Model):
    length = models.FloatField(blank=True)
    breadth = models.FloatField(blank=True)
    height = models.FloatField(blank=True)
    area = models.FloatField(blank=True)
    volume = models.FloatField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "box"
        verbose_name_plural = "boxes"

    def __str__(self):
        return f"{self.pk} {self.created_by} - {self.length, self.breadth, self.height}"

    def get_area(self):
        return 2 * (
            self.length * self.breadth
            + self.length * self.height
            + self.height * self.breadth
        )

    def get_volume(self):
        return self.length * self.breadth * self.height

    def save(self, *args, **kwargs):
        if (self.length, self.breadth, self.height):
            self.area = self.get_area()
            self.volume = self.get_volume()
            super(Box, self).save(*args, **kwargs)
