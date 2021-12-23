from django.db.models import fields
from rest_framework import serializers
from .models import *

class userSerializer(serializers.ModelSerializer):
     class Meta:
        model = Users
        fields = '__all__'