from django.db import models

class Blog(models.Model):
    title = models.TextField()
    publish_date = models.DateField()
    summary = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
