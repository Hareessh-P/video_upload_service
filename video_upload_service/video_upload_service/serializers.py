from rest_framework import serializers
from .models import Course, UserMetadata, Video


class UserMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMetadata
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'