from django.db import models
from djongo import models

# Create your models here.
class Posts(models.Model):
    user_name = models.CharField(max_length=35)
    caption = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    like = models.IntegerField(default=0)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.user_name
