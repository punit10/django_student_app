from django.db import models

# Create your models here.
class Score(models.Model):
    name = models.CharField(max_length=40)
    marks = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.name

# Score(name='Punit', marks=90).save()
# Score(name='Raju', marks=95).save()
# Score(name='Ramla', marks=85).save()
# Score(name='Rashmi', marks=75).save()
