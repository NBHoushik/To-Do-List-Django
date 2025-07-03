from django.db import models

# Create your models here.
class User_Tasks(models.Model):
  data=models.CharField()
  def __str__(self):
    return f"{self.data}"

class completed_tasks(models.Model):
  data=models.CharField()

  def __str__(self):
    return f"{self.data}"