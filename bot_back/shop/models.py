from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title
