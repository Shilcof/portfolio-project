from django.db import models

class Job(models.Model):
    #upload to images file within uploads
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
