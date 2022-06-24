from rest_framework import serializers

from .models import Direction, Doctor


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    direction = serializers.SlugRelatedField(
        many=True, slug_field='name', queryset=Direction.objects.all())

    class Meta:
        model = Doctor
        fields = (
            'id',
            'name',
            'slug',
            'direction',
            'description',
            'birthday',
            'experience',
            'sort_number',
        )


class SpecificDoctorSerializer(serializers.ModelSerializer):
    direction = DirectionSerializer(many=True)

    class Meta:
        model = Doctor
        fields = (
            'id',
            'name',
            'slug',
            'direction',
            'description',
            'birthday',
            'experience',
            'sort_number',
        )
