from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Zipcode(models.Model):
	zipcode = models.IntegerField(primary_key=True)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=2)

	def __str__(self):
		return f"{self.zipcode} {self.city} {self.state}"


class Company(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()

	def __str__(self):
		return self.name


class JobLevel(models.Model):
	level_name = models.CharField(max_length=50)

	def __str__(self):
		return self.level_name


class JobType(models.Model):
	type_name = models.CharField(max_length=50)

	def __str__(self):
		return self.type_name


class Location(models.Model):
	street_address = models.CharField(max_length=50)
	zipcode = models.ForeignKey(Zipcode, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.street_address}, {self.zipcode}"


class JobPost(models.Model):
	poster = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)
	job_level = models.ForeignKey(JobLevel, on_delete=models.CASCADE)
	post_date = models.DateField(auto_now=False, auto_now_add=False)
	job_description = models.TextField()
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)

	def __str__(self):
		return self.title



