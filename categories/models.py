from django.db import models

class Category(models.Model):
    """
    Category model, related to Post
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
