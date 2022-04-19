from distutils.command.upload import upload

from django.db import models

# Create your models here.
class Department(models.Model):

    department = models.CharField(max_length=200)

    def __str__(self):
        return self.department


class Employee(models.Model):
    image = models.ImageField(upload_to = 'employee_image/')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20)
    department_key = models.ForeignKey(Department, on_delete=models.PROTECT)