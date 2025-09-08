from django.db import models

# Create your models here.
class Gender(models.Model):
    gender = models.CharField(max_length=10)
    
    def __str__(self):
        return self.gender
    
    
class Person(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    date_birthday = models.DateField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name="person")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.gender} date of birthday {self.date_birthday}"
    