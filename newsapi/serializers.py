from django import forms
from news.models import newsData
from rest_framework import serializers


class Newsserializer(serializers.ModelSerializer):
    class Meta:
        model = newsData
        exclude=['user_id']

