from rest_framework import serializers
from django.contrib.auth.models import User
# from dataccess.models import Profile

# class ProfileSerializer(serializers.ModelSerializer):
# class ProfileSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Profile
# 		fields = ('id', 'user','userType',)

class UserSerializer(serializers.ModelSerializer):
	# profile= ProfileSerializer()
	class Meta:
		model = User
		fields = ('id', 'username', 'password', 'first_name', 'last_name')
		depth = 1

	# def create(self, validated_data):
	# 	profile_data = validated_data.pop('profile')
	# 	user = User.objects.create(**validated_data)
	# 	Profile.objects.create(user=user, **profile_data)
	# 	return user