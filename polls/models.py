from django.db import models
from django.utils import timezone

class Vote(models.Model):
    vote_name = models.CharField(default = '',max_length=20)
    created = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.vote_name

class Choice(models.Model):
    vote = models.ForeignKey(Vote,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    count = models.IntegerField(default=0)
    powerful = models.BooleanField(default=False)
    def __str__(self):
        return self.name