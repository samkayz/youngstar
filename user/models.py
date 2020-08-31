from django.db import models


class Story(models.Model):
    story = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'story'
        

class Question(models.Model):
    questn = models.TextField(null=True, blank=True)
    option1 = models.TextField(null=True, blank=True)
    option2 = models.TextField(null=True, blank=True)
    option3 = models.TextField(null=True, blank=True)
    option4 = models.TextField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'question'