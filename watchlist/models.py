from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class StreamPlatform(models.Model):
    name=models.CharField(max_length=55)    
    about=models.CharField(max_length=233)
    website= models.URLField(max_length=66)

    def __str__(self):
        return self.name

class WatchList(models.Model):
    title= models.CharField(max_length=55)
    storyline=models.CharField(max_length=255)
    avg_ratting = models.FloatField(default=0)
    number_ratting = models.IntegerField(default=0)
    active=models.BooleanField()
    created= models.DateTimeField(auto_now_add=True)
    platform= models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist')

    def __str__(self):
        return self.title

class Review(models.Model):
    rating = models.PositiveIntegerField(validators= [MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=255,null=True)
    reviewed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_detail')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return str(self.rating)+" : "+self.watchlist.title

