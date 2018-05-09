# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from models import Menu, RawMaterial, Green
from serializers import MenuSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class MenuList(APIView):

    def get(self, request, format=None):
        menu_list = []
        green_list = Green.objects.all()
        if green_list:
            for green in green_list:
                menu_list.append(green.menu.name)
        return Response(menu_list, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        pass
