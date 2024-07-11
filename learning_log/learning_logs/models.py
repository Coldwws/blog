from django.utils import timezone
from django.db import models


class Topic(models.Model):
    '''Это поле которое хранит название темы'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.text

class Entry(models.Model):
    '''информация по пользовательской теме'''

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return f'{self.text[:50]}...'

class Comment(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.entry.topic}: {self.text[:50]}'