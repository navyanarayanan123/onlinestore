from django.db import models
from django.contrib.auth.models import User
from owner.models import Books

# Create your models here.
class Employee(models.Model):
 emp_name= models.CharField(max_length=120)
 desig=models.CharField(max_length=100)
 exp=models.PositiveIntegerField()
 salary=models.PositiveIntegerField()


 def __str__(self):
  return self.emp_name
# # cart item,user,date,status
# # model relationships
# # 1.one to one
# # 2.one to many
class Cart(models.Model):
 user=models.ForeignKey(User,on_delete=models.CASCADE)
 item=models.ForeignKey(Books,on_delete=models.CASCADE)
 date=models.DateField(auto_now_add=True)
 options=(
  ('incart','incart'),
  ('cancelled','cancelled'),
  ('order placed','order placed')
 )
 status=models.CharField(max_length=120,choices=options,default="incart")

class Orders(models.Model):
 user = models.ForeignKey(User,on_delete=models.CASCADE)
 item=models.ForeignKey(Books,on_delete=models.CASCADE)
 delivery_address=models.CharField(max_length=200)
 contact_number=models.CharField(max_length=15)
 date = models.DateField(auto_now_add=True)
 options=(
  ('order placed','order placed'),
  ('order cancelled','order cancelled'),
  ('dispatched','dispatched'),
  ('in-transit','in-transit'),
  ('delivered','delivered')
 )
 status=models.CharField(max_length=120,choices=options,default="order placed")