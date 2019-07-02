from django.db import models
from django.urls import reverse
import datetime
import uuid

# Create your models here.


class Car(models.Model):
    """
    Represeting a car
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Уникальный ID автомобиля")

    reg_id = models.CharField(
        max_length=12, help_text="Регистрационный номер автомобиля")
    model = models.CharField(max_length=20, help_text="Марка автомобиля")

    def __str__(self):
        return f"{self.model} ({self.reg_id})"


class Platform(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Уникальный ID площадки")

    address = models.CharField(max_length=150, help_text="Адрес площадки")

    def __str__(self):
        return f"Площадка ({self.address})"


class ChecklistType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Уникальный ID типа чеклиста")

    label = models.CharField(max_length=50, help_text="Название типа")

    def __str__(self):
        return self.label


class AnswerType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Уникальный ID типа ответа")

    label = models.CharField(max_length=50, help_text="Название типа")

    def __str__(self):
        return self.label


class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Уникальный ID ответа")

    label = models.CharField(max_length=50, help_text="Текст ответа")

    type = models.ForeignKey('AnswerType', on_delete=models.SET_NULL,
                             null=True, help_text="Тип ответа")

    def __str__(self):
        return self.label


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Уникальный ID вопроса")

    label = models.CharField(max_length=300, help_text="Текст вопроса")

    answers = models.ManyToManyField(
        Answer, help_text="Выберите ответы для вопроса")

    parent_question = models.ForeignKey(
        'Question', on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular question instance
        """
        return reverse('question-detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.label} ({'/'.join(map(str, self.answers.all()))})"


class Checklist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Уникальный ID чеклиста")

    label = models.CharField(max_length=300, help_text="Текст заголовка")

    type = models.ForeignKey(
        'ChecklistType', on_delete=models.CASCADE)

    questions = models.ManyToManyField(
        Question, help_text="Выберите вопросы дляя чеклиста")

    def __str__(self):
        return f"{self.label} ({self.type}, {self.id})"


class Staff(models.Model):
    position = models.CharField(
        max_length=150, help_text="Должность сотрудника")
    name = models.CharField(
        max_length=150, help_text="Фамилия и инициалы сотрудника")

    def __str__(self):
        return self.name


class ChecklistEntity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Уникальный ID чеклиста")
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(default=datetime.datetime.now())

    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)

    def __str__(self):
        return self.checklist.label


class FilledChecklistEntity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Уникальный ID чеклиста")

    checklist_entity = models.ForeignKey(
        ChecklistEntity, on_delete=models.CASCADE)

    def __str__(self):
        return self.checklist_entity.checklist.label
