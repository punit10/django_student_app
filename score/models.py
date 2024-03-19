from django.db import models

# Create your models here.
class Score(models.Model):
    name = models.CharField(max_length=40)
    marks = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.name

#set default field of order in which it will show 
    class Meta:
        ordering = ['name']

# Score(name='Punit', marks=90).save()
# Score(name='Raju', marks=95).save()
# Score(name='Ramla', marks=85).save()
# Score(name='Rashmi', marks=75).save()
