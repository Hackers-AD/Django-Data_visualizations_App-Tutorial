from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DataSet(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	label=models.CharField(max_length=30)
	value=models.IntegerField(default=0)
