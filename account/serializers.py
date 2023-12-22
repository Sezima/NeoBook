from django.contrib.auth import authenticate

from rest_framework import serializers

from .models import MyUser
from .utils import send_welcome_email


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=6, write_only=True)
    password_confirm = serializers.CharField(min_length=6, write_only=True)

    def validate(self, data):
        password = data.get('password')
        password_confirm = data.get('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError('Passwords do not match.')

        return data

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        username = validated_data.get('username')

        user = MyUser.objects.create_user(email=email, password=password, username=username)
        user.create_activation_code()
        user.save()
        send_welcome_email(email=user.email, activation_code=user.activation_code)
        return user






class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        label='Password',
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if not user:
                message = 'Unable to login'
                raise serializers.ValidationError(message, code='authorization')
        else:
            message = 'Must include "email" and "password".'
            raise serializers.ValidationError(message, code='authorization')

        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email', 'avatar', 'id', 'followers', 'followings')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['followers'] = instance.followers.count()
        representation['followings'] = instance.followings.count()

        return representation


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['email']


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username']




