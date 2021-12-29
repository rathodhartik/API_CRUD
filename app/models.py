from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField()
    age=models.IntegerField()
    subject=models.CharField(max_length=100,null=False)
    

<<<<<<< HEAD
    marks=models.IntegerField(null=False)
    
=======
    marks=models.IntegerField()
    marks2=models.IntegerField()

>>>>>>> ri
    def __str__(self):
        return self.name