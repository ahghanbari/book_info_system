from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=400)
    pub_date = models.DateField()
    pages_number = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()

    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title