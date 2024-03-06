from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


STATUS= (
   ('UN', 'Unlisted'),
   ('L', 'Live'),
   ('S', 'Sold')
)
CONDITION= (
   ('G','Good'),
   ('VG','Very Good'),
   ('P', 'Pristine')
)

class Ring(models.Model):
  name = models.CharField(max_length=250)
  status = models.CharField(
     choices = STATUS,
     default=STATUS[0][0]
  )
  size = models.IntegerField()
  metal = models.CharField(max_length=250)
  stone = models.CharField(max_length=250)
  condition = models.CharField(
    #  condition should link to CONDITION - need to adjust
     choices = STATUS,
     default=STATUS[0][0]
  )
  weight = models.IntegerField()
  price = models.IntegerField()
  purchase_point = models.CharField(max_length=250)
  purchase_date = models.DateField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
      return f"{self.name}, sz {self.size}, status {self.status}"
  
  def get_absolute_url(self):
      return reverse("ring_detail", kwargs={"ring_id": self.id})
  
  