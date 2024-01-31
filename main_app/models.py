from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
    ('B', 'Breakfast'),
    ('D', 'Dinner'),
)

class Toy(models.Model):
    name= models.CharField(max_length=100)
    color= models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})
    
# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})
    
class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']