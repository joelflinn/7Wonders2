from django.db import models
from django.urls import reverse


# Create your models here.
class Board(models.Model):
    WIN_OR_LOSS = (
        ('WIN', 'win'),
        ('LOSS', 'loss')
    )

    name = models.CharField(max_length=200)
    board_type = models.CharField(max_length=200)
    win_or_loss = models.CharField(max_length=200, choices= WIN_OR_LOSS)
    score = models.PositiveBigIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('7wonders', args=[str(self.id)])
    

class Card(models.Model):
    name = models.CharField(max_length=200)

    add_to_board = models.BooleanField(default=False)
    pointValue = models.PositiveBigIntegerField(default=0)
    card_image = models.ImageField(default=None)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('7wonders', args=[str(self.id)])
    
class InstanceCards(models.Model):
    name = models.CharField(max_length=200)

    add_to_board = models.BooleanField(default=False)
    pointValue = models.PositiveBigIntegerField(default=0)
    board = models.ForeignKey(Board, on_delete=models.CASCADE,null = True)
    card_image = models.ImageField(default=None)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('7wonders', args=[str(self.id)])