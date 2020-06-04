from django.db import models
import datetime
# Create your models here.
class Destinations(models.Model):
	name = models.CharField(max_length=100);
	price = models.IntegerField();
	desc = models.TextField();
	img = models.ImageField(upload_to = 'pics');
	offer = models.BooleanField(default=False);