from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class T(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	train_name = models.CharField(max_length=40)
	train_no = models.CharField(max_length=6, unique=True)
	starting_at = models.CharField(max_length=30)
	ending_at = models.CharField(max_length=30)
	created_at = models.DateTimeField(auto_now_add=True)
	d_date = models.DateTimeField()
	updated_at = models.DateTimeField(auto_now =True)

	def __str__(self):
		return self.train_name



class B(models.Model,):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	train_name = models.ForeignKey(T,on_delete=models.CASCADE)
	#print("enter number of tickets")
	passenger_name = models.CharField(max_length=40)
	aaddhar_no =models.CharField(max_length=12)

	def __str__(self):
		return self.passenger_name