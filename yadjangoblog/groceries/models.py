# coding=utf-8
# from django.contrib.auth.models import User
from django.contrib.gis.db import models


class CompanyCategory(models.Model):
    name = models.CharField(verbose_name="分类", db_index=True, unique=True, null=False, blank=False, max_length=100)
    order_num = models.IntegerField(verbose_name="排序", default=0, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "公司分类"
        verbose_name_plural = "公司分类"
        app_label = '网站合集'

class Company(models.Model):
    name = models.CharField(verbose_name="公司名", db_index=True, unique=True, null=False, blank=False, max_length=100)
    logo = models.ImageField(upload_to="logos", default=None)
    desc = models.CharField(verbose_name="描述", max_length=100)
    category = models.ForeignKey(CompanyCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "公司"
        verbose_name_plural = "公司"
        app_label = '网站合集'