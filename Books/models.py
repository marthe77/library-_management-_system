from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classroom = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=3, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to="", blank=True)

class Book_Issue(models.Model):
    student = models.ForeignKey('Students', on_delete=models.CASCADE)
    Books = models.ForeignKey('Book', on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now=True)
    return_date = models.DateTimeField()
    remarks = models.CharField(max_length=100, default="Some Remarks")

     