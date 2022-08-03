class Employee(models.Model):
 emp_name= models.CharField(max_length=120)
 desig=models.CharField(max_length=100)
 exp=models.PositiveIntegerField()
 salary=models.PositiveIntegerField()


 def __str__(self):
  return self.emp_name