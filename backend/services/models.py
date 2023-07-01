from django.db import models


class CloudService(models.Model):
    name: str = models.CharField(max_length=50)
    number_of_service: int = models.PositiveIntegerField()
    number_of_region: int = models.PositiveIntegerField()
    number_of_availability_zone: int = models.PositiveIntegerField()

    def __str__(self):
        return self.name
