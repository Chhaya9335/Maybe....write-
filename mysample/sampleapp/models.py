from django.db import models


# Create your models here.


class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5 stars
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f"{self.name} - {self.rating}⭐"


from django.db import models

class Contribution(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]  # Show first 50 chars
