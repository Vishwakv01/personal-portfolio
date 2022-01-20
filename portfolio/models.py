from django.db import models


class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    thumbline = models.ImageField(upload_to='portfolio')
    link = models.URLField(blank=True)


