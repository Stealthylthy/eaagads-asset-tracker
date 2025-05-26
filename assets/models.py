from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Asset(models.Model):
    serial_number = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    purchase_date = models.DateField()

    def __str__(self):
        return self.name

class Maintenance(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    scheduled_date = models.DateField()
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.asset.name} - {self.scheduled_date}"
    
class Staff(models.Model):
     name = models.CharField(max_length=100)
     email = models.EmailField()
     department = models.ForeignKey(Department, on_delete=models.CASCADE)

     def __str__(self):
        return f"{self.name} ({self.department.name})"

