from django.db import models

# Create your models here.

class Student(models.Model):
    """
    This class represents an instance of student.
    """
    name = models.CharField(max_length=254)
    roll = models.CharField(max_length=254)
    image = models.ImageField(upload_to='students')

    def __str__(self):
        return self.name
    
class WasteType(models.Model):
    """
    This class represents an instance of waste type.
    
    """
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField(upload_to='waste_type')

    def __str__(self):
        return self.name
    
class FoodWaste(models.Model):
    """
    This class represents an instance of food waste.
    """
    name = models.CharField(max_length=254)
    type = models.ForeignKey(WasteType, on_delete=models.CASCADE)
    description = models.TextField()
    source = models.CharField(max_length=254)
    where_to_throw = models.CharField(max_length=254)
    image = models.ImageField(upload_to='food_waste')
    time_to_decay = models.CharField(max_length=254)
    carbon_footprint = models.CharField(max_length=254)
    added_by = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


