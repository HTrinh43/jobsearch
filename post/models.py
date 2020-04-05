from django.db import models
from django.contrib.auth.models import User

WORKTIME_CHOICE = [
	('FULL','Fulltime'),
	('PART','Parttime'),
	('FULLandPART', 'Fulltime and Parttime'),
	]
class Post(models.Model):
	job = models.CharField(max_length=255, default=None)
	workplace = models.CharField(max_length=255, default=None)
	worktime = models.CharField(max_length=255, default=None, choices=WORKTIME_CHOICE)
	address = models.TextField(default=None)
	salary = models.IntegerField(default=None)
	description = models.TextField(default=None)
	author = models.ForeignKey(User, on_delete = models.CASCADE, default = None)
	pub_date = models.DateTimeField(default=None)

	def __str__(self):
		return self.job

	def job_type(self):
		return self.worktime

	def salary_display(self):
		return '$' + str(self.salary) + '/h' 

