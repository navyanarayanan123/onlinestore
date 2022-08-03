from django.db import models

# Create your models here.
books=[
   {"id": 100,"book_name":"randamoozham","author":"mt","price":480,"copies":250},
    {"id":101,"book_name": "aarachar", "author": "meera", "price": 580, "copies": 250},
    {"id":102,"book_name": "the alchemist", "author": "paulo", "price": 780, "copies": 250},
    {"id":103,"book_name": "rainrising", "author": "nirupama", "price": 1000, "copies": 250},
    {"id":104,"book_name": "indhuleka", "author": "chandhu menon", "price": 280, "copies": 250},
    {"id":105,"book_name": "pazhassy", "author": "mt", "price": 580, "copies": 350},

]
# create a table Book(book_name varchar(255), author varchar(60),copies int(),price int())
class Books(models.Model):
 book_name= models.CharField(max_length=120,unique=True)
 author=models.CharField(max_length=100)
 price=models.PositiveIntegerField()
 copies=models.PositiveIntegerField()
 published_date=models.DateField(null=True)
 image=models.ImageField(upload_to='images',null=True)

 def __str__(self):
  return self.book_name

class Employee(models.Model):
 emp_name= models.CharField(max_length=120)
 desig=models.CharField(max_length=100)
 exp=models.PositiveIntegerField()
 salary=models.PositiveIntegerField()


 def __str__(self):
  return self.emp_name


# CRUD operations
# ORM for creating new book object
# C-CREATE
# ref = ModelName(field=value,field=value,...)
# ref.save()
# book=Books(book_name="book1",author="author1",price=130,copies=20)
# book.save()

# R-RETRIEVE
# fetching all objects
# ref=ModelName.objects.all()
# books=Books.objects.all()
qs=Books.objects.filter(price__lt=500)
# U-UPDATE
# update copies of book rainrising
# >>> qs=Books.objects.get(id=7)
# >>> qs
# <Books: rainrising>
# >>> qs.copies=50
# >>> qs.save()


# D-DELETE
# delete all objects
# modelname.objects.all().delete()

# to delete particular book object
# >>> qs=Books.objects.get(id=6)
# >>> qs.delete()
# (1, {'owner.Books': 1})

# book object except mt
# qs=Books.objects.all().exclude(author="mt")

# books name starts with ra
# qs=Books.objects.filter(book_name__startswith="ra")

# books name ends with a
#  qs=Books.objects.filter(author__endswith="a")

# books name contains ha
# qs=Books.objects.filter(book_name__contains="ha")
# >>> qs
# <QuerySet [<Books: randamoozham>, <Books: aarachar>, <Books: indhulekha>]>

# get a specific book
# >>> qs=Books.objects.get(id=4)
# >>> qs
# <Books: randamoozham>

