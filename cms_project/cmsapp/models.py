from django.db import models

class AddModel(models.Model):
	Subject = models.CharField(max_length=30)
	Assignment = models.CharField(max_length=30)
	RMaterial = models.FileField()

	def __str__(self):
		return str(self.Subject)

class UploadModel(models.Model):
	name = models.CharField(max_length=30)
	prn = models.IntegerField(primary_key = True)
	subject = models.CharField(max_length=30)
	Submission = models.FileField()

	def __str__(self):
		return str(self.prn)
	