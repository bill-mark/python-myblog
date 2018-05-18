from django.db import models

# Create your models here.

class Artical(models.Model):
    title = models.CharField(max_length=32,default='title')
    content = models.TextField(null=True)

    def __str__(self):
        return self.title


class ArticalTest(models.Model):
    title = models.CharField(max_length=32,default='title')
    content = models.TextField(null=True)

    def __str__(self):
        return self.title