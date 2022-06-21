from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Videos(models.Model):
    title = models.CharField( max_length=255)
    desc = models.TextField()
    publishing_date = models.DateTimeField()
    url_for_thumnail = models.URLField(max_length=255)
    link = models.URLField(max_length=255)

    class Meta:
        ordering = ["-publishing_date"]  # To sort in reverse chronological order
    def __str__(self):
        return self.title
