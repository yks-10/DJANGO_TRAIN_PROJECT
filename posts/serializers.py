from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
class PostSerializer(serializers.ModelSerializer):
	class Meta:
	    fields = ('id', 'user', 'train_name', 'train_no', 'starting_at', 'ending_at', 'created_at', 'd_date')
	    model = T

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)


class BSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'user', 'train_name', 'passenger_name', 'aaddhar_no')
        model = B