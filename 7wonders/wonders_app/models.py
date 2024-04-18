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
        return reverse('portfolio', args=[str(self.id)])