from django.db import models

# Create your models here.
class Departments(models.Model):
    departmentName = models.CharField(max_length=100)
    departmentSummary = models.TextField()
    
    def __str__(self) -> str:
        return self.departmentName

class Doctors(models.Model):
    doctorName = models.CharField(max_length=250)
    doctorSpec = models.CharField(max_length=250)
    departmentName = models.ForeignKey(Departments, on_delete=models.CASCADE)
    doctorImage = models.ImageField(upload_to='doctors')
    
        