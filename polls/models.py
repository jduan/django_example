import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    # class fields represent table columns
    # The name of each Field instance is the column's name
    question_text = models.CharField(max_length=200)
    # The 'data published' is the human_readable name
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        past = now - datetime.timedelta(days=1)
        return past <= self.pub_date < now


class Choice(models.Model):
    question_text = models.ForeignKey(Question, on_delete=models.CASCADE)
    # some field like CharField requires you give it a max_length
    # it's used by the database as well as validation
    choice_text = models.CharField(max_length=200)
    # default is an optional argument, unlike max_length above
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
