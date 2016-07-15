from django.db import models

# Create your models here.

class AnimeTitle(models.Model):
	img = models.CharField(max_length = 120)
	title = models.CharField(max_length = 120)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	release_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
	class Meta:
		ordering = ['release_time']
	def __str__(self):
		return self.title



class Episode(models.Model):
	title = models.CharField(max_length = 120)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	AnimeTitle = models.ForeignKey(AnimeTitle)
	p480 = models.CharField(max_length = 120)
	p720 = models.CharField(max_length = 120)
	p1080 = models.CharField(max_length = 120)
	sub_file = models.CharField(max_length = 120)
	def __str__(self):
		return self.title
	class Meta:
		ordering = ['-timestamp']

class Schedule(models.Model):
	title = models.CharField(max_length = 120)
	AnimeTitles = models.ManyToManyField(AnimeTitle)






