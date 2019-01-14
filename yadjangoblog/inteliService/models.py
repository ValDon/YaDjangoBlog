# from django.db import models

from django.contrib.gis.db import models


class Question_Answer(models.Model):
    qa_id = models.IntegerField()
    question = models.TextField()
    answer = models.TextField()
    match_nums = models.IntegerField()

    # def __str__(self):
    #     return self.name

    # class Meta:
    #     verbose_name = "公司分类"
    #     verbose_name_plural = "公司分类"
    #     app_label = 'groceries'

class User_Question(models.Model):
    user_id = models.IntegerField(default=1)
    user_question = models.TextField()
    match_flag = models.TextField()
    match_question_id = models.IntegerField()
    match_score = models.FloatField()
