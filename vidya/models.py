from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    quote = models.CharField(max_length=100)
    description = models.TextField()
    thumb = models.ImageField(upload_to='image/')
    file = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title