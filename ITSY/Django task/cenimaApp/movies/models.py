from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=100)
    protagonists = models.TextField()
    poster = models.ImageField(upload_to='posters/')
    trailer = models.URLField()
    start_date = models.DateTimeField()
    STATUS_CHOICES = [
        ('coming_up', 'Coming Up'),
        ('starting', 'Starting'),
        ('running', 'Running'),
        ('finished', 'Finished'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    ranking = models.IntegerField(default=0)
