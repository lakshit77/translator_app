from django.db import models

# Create your models here.

language_choice = [
    ("hi", "Hindi"),
    ("gu", "Gujarati"),
    ("th", "Telegu"),
    ("ta", "Tamil"),
    ("es", "Spanish"),
    ("mr", "Marathi")
]
class TranslationLog(models.Model):
    input_text = models.TextField()
    output_text = models.TextField()
    language_used = models.CharField(max_length=200, choices=language_choice)
    created_at = models.DateTimeField(auto_now=True)

    # def __str__(self) -> str:
    #     return self.title