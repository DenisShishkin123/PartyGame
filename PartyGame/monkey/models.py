from django.db import models
from django.urls import reverse_lazy

# Create your models here.

# card
# action

class Card(models.Model):

    # number = id (pk)
    action = models.TextField("действие")

    def __str__(self):
        return self.action

    def get_absolute_url(self):
        # return reverse_lazy("card", self.pk)
        return reverse_lazy("card", kwargs={"pk": self.pk})
        # return reverse('myurl', kwargs={'id': self.id, 'name': self.name})






