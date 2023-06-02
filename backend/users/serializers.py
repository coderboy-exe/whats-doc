from rest_framework import viewsets, serializers

from .models import User

MIN_LENGTH = 8

class UserSerializer(serializers.ModelSerializer):
    """User serializer"""
    password = serializers.CharField(
        write_only=True,
        min_length=MIN_LENGTH,
        error_messages={
            "min_length": f"Password must be at least {MIN_LENGTH} characters"
        }
    )
    
    password2 = serializers.CharField(
        write_only=True,
        min_length=MIN_LENGTH,
        error_messages={
            "min_length": f"Password must be at least {MIN_LENGTH} characters"
        }
    )

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Passwords do not match.")
        return data
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            is_active=validated_data["is_active"],
            is_doctor=validated_data["is_doctor"],
            is_patient=validated_data["is_patient"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user