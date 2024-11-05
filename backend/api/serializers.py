from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note, UserProfile


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True, max_length=30)
    last_name = serializers.CharField(required=True, max_length=30)
    email = serializers.EmailField(required=True)
    phone_number = serializers.CharField(required=True, max_length=15)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "password",
            "confirm_password",
        ]

    def validate(self, data):
        # Проверка совпадения пароля и подтверждения пароля
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Пароли не совпадают")

        # Проверка уникальности номера телефона
        if UserProfile.objects.filter(phone_number=data["phone_number"]).exists():
            raise serializers.ValidationError("Этот номер телефона уже зарегистрирован")

        return data

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                "Этот логин уже используется другим пользователем"
            )
        return value

    def create(self, validated_data):
        # Удаляем поле подтверждения пароля, так как оно не нужно для создания пользователя
        validated_data.pop("confirm_password")
        phone_number = validated_data.pop("phone_number")

        # Создание пользователя с передачей необходимых полей
        user = User.objects.create_user(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

        # Создание профиля пользователя с номером телефона
        UserProfile.objects.create(user=user, phone_number=phone_number)

        return user


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}
