from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import tareas

# Create your views here.
class TareasVistas(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = tareas.objects.all()
