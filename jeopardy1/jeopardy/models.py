from django.db import models


class Category(models.Model):
	id = models.CharField(max_length=30, primary_key=True)
	title = models.CharField(max_length=30)
	clues_count = models.IntegerField()



# Create your models here.
