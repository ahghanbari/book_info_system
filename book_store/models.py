from django.db import models
from django.urls import reverse
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=400)
    pub_date = models.DateField()
    pages_number = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])