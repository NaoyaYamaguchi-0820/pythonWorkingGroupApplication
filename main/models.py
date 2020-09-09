from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Employee(models.Model):

    employeeID = models.IntegerField(
        verbose_name='社員番号',
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(99999)],
    )

    name = models.CharField(
        verbose_name='名前',
        max_length=20,
    )

    age = models.IntegerField(
        verbose_name='年齢',
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(150)],
    )

