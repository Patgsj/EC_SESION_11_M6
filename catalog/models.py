from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    rating = models.FloatField()

    def get_rating_level(self):
        if self.rating < 1000:
            return "Baja"
        elif 1000 <= self.rating <= 2500:
            return "Media"
        else:
            return "Alta"

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_manage_books", "Can manage books"),
        ]


# Create your models here.
