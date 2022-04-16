from django.db import models

class dict(models.Model):
    letter = models.CharField(max_length = 30)
    word = models.CharField(max_length = 30)
    defi = models.CharField(max_length = 30)
    example = models.CharField(max_length = 30)

def __str__(self):
    return "%s  %s"%(self.letter,self.word)
