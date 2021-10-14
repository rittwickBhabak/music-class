from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=1000)
    youTubeVideoID = models.CharField(max_length=1000, blank=True, null=True)
    lyricsURL = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title