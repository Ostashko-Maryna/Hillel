import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    question_text_long = models.CharField(max_length=5200, default=None)
    views = models.IntegerField(default=0)

    def __str__(self):
        return "{} publicated at {}".format(self.question_text, self.pub_date)

    @property
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "{} voted {} times".format(self.choice_text, self.votes)

