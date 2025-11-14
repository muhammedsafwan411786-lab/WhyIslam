from django.db import models

class Verse(models.Model):
    surah_name = models.CharField(max_length=100)
    ayah_number = models.IntegerField()
    arabic = models.TextField()
    urdu = models.TextField()
    english = models.TextField()

    
    # Tafsir optional hai
    tafsir_text = models.TextField(blank=True, null=True)
    tafsir_video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.surah_name} - {self.ayah_number}"

    