from rest_framework import viewsets, serializers

from .models import User, Appointment

MIN_LENGTH = 8

class UserSerializer(serializers.ModelSerializer):
    # """User serializer"""

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            is_patient=validated_data['is_patient'],
            is_doctor=validated_data['is_doctor']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class AppointmentSerializer(serializers.ModelSerializer):
    """ Appointment serializer class """

    class Meta:
        model = Appointment
        fields = '__all__'