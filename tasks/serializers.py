from rest_framework import serializers
from .models import Task


# Provides a set of default implementations for commonly used serialization tasks.
class TaskSerializer(serializers.ModelSerializer):
    class Meta: # Metadata for the serializer
        model = Task
        fields = '__all__'
        read_only_fields=['user']