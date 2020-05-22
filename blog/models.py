from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    body = models.TextField(default=None)
    image = models.ImageField(upload_to='images/')

    # displays title in admin
    def __str__(self):
        return self.title

    # limits length of body
    def summary(self):
        return self.body[:40] + (self.body[40:] and '...')

    # shorten date
    def publish_date_nice(self):
        return self.publish_date.strftime('%e %b %Y')
