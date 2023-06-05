from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"Tag '{self.title}', id: {self.id}"
