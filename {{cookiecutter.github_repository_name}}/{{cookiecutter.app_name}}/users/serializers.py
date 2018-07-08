from allauth.account.adapter import get_adapter
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer, ValidationError


User = get_user_model()


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_email(self, email):
        return get_adapter().validate_unique_email(email)

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'email': self.validated_data.get('email', '')
        }

    def save(self, request):
        password = self.validated_data.pop('password1', None)
        cleaned_data = self.get_cleaned_data()
        user = User.objects.create(**cleaned_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(Serializer):
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def _validate_email(self, email, password):
        # Should return 404 if no user found with this email
        # This is intentional as per requirements and specification
        user = get_object_or_404(User, email__iexact=email)
        if user and user.check_password(password):
            return user

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = self._validate_email(email, password)
        else:
            msg = _('Must include "email" and "password".')
            raise ValidationError(msg)

        if not user:
            msg = _('Unable to log in with provided credentials.')
            raise ValidationError(msg)

        if not user.is_active:
            msg = _('User account is disabled.')
            raise ValidationError(msg)

        # Everything passed. That means password is accepted. So return the user
        attrs['user'] = user
        return attrs


class UserDetailsSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'is_superuser')
        read_only_fields = ('is_superuser',)


class UserPublicSerializer(ModelSerializer):

    full_name = serializers.CharField(source='get_full_name')

    class Meta:
        model = User
    fields = ('id', 'full_name', 'email')
