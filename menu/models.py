# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class RawMaterial(models.Model):
    """
    原材料
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    describe = models.TextField(max_length=100)
    menu = models.ManyToManyField(Menu, related_name="menu", on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_time',)

    def __unicode__(self):
        return self.name


class Menu(models.Model):
    """
    菜谱
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    describe = models.TextField(max_length=100)

    class Meta:
        ordering = ('created_time',)

    def __unicode__(self):
        return self.name


class Green(models.Model):
    """
    菜
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    describe = models.TextField(max_length=100)
    menu = models.OneToOneField(Menu)

    class Meta:
        ordering = ('created_time',)

    def __unicode__(self):
        return self.name




