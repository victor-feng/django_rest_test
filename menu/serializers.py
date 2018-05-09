# -*- coding:utf-8 -*-

from rest_framework import serializers
from models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        field = ['id', 'name', 'created_time', 'describe']

