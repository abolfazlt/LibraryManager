from django.db import models
from django.urls import reverse


class EFile(models.Model):
    file_name = models.CharField(max_length=100)
    file_author = models.CharField(max_length=100)
    file_content = models.FileField(max_length=500, default='')

    def get_absolute_url(self):
        return reverse('EFiles:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.file_name + '-' + self.file_author
