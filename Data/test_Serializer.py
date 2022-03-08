from concurrent.futures.process import EXTRA_QUEUED_CALLS
from dataclasses import field
import email
from enum import unique
from unittest.util import _MAX_LENGTH
from django.forms import PasswordInput
from rest_framework import serializers

from Data import models

class test_serializer(serializers.Serializer):
    name=serializers.CharField(max_length=10)
    email=serializers.EmailField(max_length=20)
    password=serializers.CharField(max_length=100,write_only=True,required=True)

class use_test_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.DataBase
        fields=("id","mail","name","password")
        extra_kwargs={
        "pasword":{
        "write_only":True,
        "style":{
            "input_type":"password"
        }}}
    def create(self, validated_data):
        models.DataBase.objects.create_user(mail=validated_data['mail'],name=validated_data['name'],password=validated_data['password'])
        return super().create(validated_data)
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
 
        return super().update(instance, validated_data)