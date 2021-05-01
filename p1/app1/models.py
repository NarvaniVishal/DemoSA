from django.db import models

# Create your models here.

class Course(models.Model):
	name=models.CharField(max_length=100,null=True)
	no=models.IntegerField(null=True)

class Student(models.Model):
	no=models.IntegerField(null=True)
	name=models.CharField(max_length=100,null=True)
	stu_img=models.ImageField(upload_to='images',null=True)
	birth_Date=models.DateField(null=True)
	email_id=models.EmailField(null=True)
	perc=models.FloatField(null=True)
	df=models.DurationField(null=True)
	tf=models.TimeField(null=True)
	stu_course=models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)
	
	def __str__(self):
		return str(self.no)+ " : " + self.name


