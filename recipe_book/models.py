from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Recipe(models.Model):

	recipe_name = models.CharField(max_length=100)
	description = models.TextField()
	instructions = models.TextField()
	date_created = models.DateTimeField(default=timezone.now)
	date_updated = models.DateField(auto_now=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.recipe_name

	# create get_absolute_url method so django redirects to DetailView when new recipe is created.
	def get_absolute_url(self):
		return reverse('recipe-detail', kwargs={'pk': self.pk})
		#use the reverse function which returns a string of the desired url so that the view
		#can redirect



