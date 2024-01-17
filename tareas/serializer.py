from rest_framework import serializers
from .models import tareas

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = tareas
        # fields = ('id', 'tilte', 'descripcion', 'done')
        fields = '__all__'