from rest_framework import serializers
from . models import Register
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators = [UniqueValidator(queryset=Register.objects.all())]
    )
    mobile = serializers.CharField(required=True)
    password = serializers.CharField(required = True,validators = [validate_password] )
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = Register
        fields = ['name','email','mobile','password','confirm_password']
        extra_kwargs = {
            'name':{'required':True},
            'mobile':{'required':True}
        }
    def validate(self,attrs):
        if attrs['password'] != attrs ['confirm_password']:
            raise serializers.ValidationError({"password":"Password fields didn't match"})
        if len(attrs['password']) < 8:
            raise serializers.ValidationError({"password":"Length of the password should atleast be 8"})
        return attrs
    def create(self,validated_data):
        register = Register.objects.create(
            name = validated_data['name'],
            email = validated_data['email'],
            mobile = validated_data['mobile'],
            password = validated_data['password'],
            confirm_password = validated_data['confirm_password']
        )
      
        register.save()

        return register
