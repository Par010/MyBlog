from django.db import models

# Create your models here.
class Postt(models.Model):

    title = models.CharField(max_length=80)
    publish_date = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title

    def publish_date_simplified(self):
        return self.publish_date.strftime('%b %e %Y')

    def summary(self):
        if len(self.text) <= 100:
            return self.text
        else:
            return self.text[:100] + '...'
