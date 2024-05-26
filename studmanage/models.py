from django.db import models



class Student(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  date_of_birth = models.DateField()
  email = models.EmailField(unique=True)
  street = models.CharField(max_length=255)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  pincode = models.CharField(max_length=6)
  subjects = models.JSONField(default=list)
  previous_schooling = models.JSONField(default=list, null=True)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"
