from django.db import models
import uuid
import django.utils
import datetime
# Create your models here.


class Question(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Answer(models.Model):
    name = models.CharField(max_length=20)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


def __str__(self):
    return self.name


class Quiz(models.Model):
    name = models.CharField(max_length=250)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name


class QuizInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(default=django.utils.timezone.now())
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    answers = models.ManyToManyField(Answer)

    def __str__(self):
        return f"{self.quiz} ({self.id})"
