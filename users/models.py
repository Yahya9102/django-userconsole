from django.db import models

# Create your models here.

class User(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False,
        help_text="Användarnman måte vara unik/inte tom"

    )

    def __str__(self):
        return self.name