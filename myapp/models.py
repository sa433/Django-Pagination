from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=70)
    desc = models.TextField(max_length=7000)
    publish_date = models.DateField()


