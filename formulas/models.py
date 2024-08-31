from django.db import models
from django.urls import reverse


class Formula (models.Model):
    name = models.CharField(max_length=20)
    name_formulas = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=300, help_text='describe the formula')
    link = models.CharField(max_length=20, default=5)
    icon_name = models.CharField(max_length=20, default=5)
    style = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name