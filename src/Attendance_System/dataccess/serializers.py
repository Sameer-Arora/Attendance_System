from rest_framework import serializers
from .models import Profile

class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ('id', 'username', 'password', 'first_name', 'last_name','userType')