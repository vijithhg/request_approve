from django.db import models

# Create your models here.
class LeaveRequest(models.Model):
    Start_date = models.DateField()
    End_date = models.DateField()
    Matter = models.TextField()
    status = models.BooleanField(default=False)