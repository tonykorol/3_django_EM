from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Dog(models.Model):
    name = models.CharField()
    age = models.IntegerField()
    breed = models.ForeignKey("Breed", on_delete=models.CASCADE)
    gender = models.CharField()
    color = models.CharField()
    favorite_food = models.CharField()
    favorite_toy = models.CharField()


class Breed(models.Model):
    CHOICES = {"T": "Tiny", "S": "Small", "M": "Medium", "L": "Large"}

    BREED_MAX_MIN_VALUES = [MinValueValidator(1), MaxValueValidator(5)]

    name = models.CharField()
    size = models.CharField(choices=CHOICES)
    friendliness = models.IntegerField(validators=BREED_MAX_MIN_VALUES)
    trainability = models.IntegerField(validators=BREED_MAX_MIN_VALUES)
    shedding_amount = models.IntegerField(validators=BREED_MAX_MIN_VALUES)
    exercise_needs = models.IntegerField(validators=BREED_MAX_MIN_VALUES)

    def __str__(self):
        return self.name
