# DRF components for creating views, managing permissions, and filtering
from rest_framework import viewsets, permissions, filters

# Used to return HTTP responses
from rest_framework.response import Response

# Used for JWT authentication
from rest_framework_simplejwt.views import TokenObtainPairView

# Provides filtering capabilities
from django_filters.rest_framework import DjangoFilterBackend

# The model representing a task
from .models import Task

# The serializer for the `Task` model
from .serializers import TaskSerializer

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet): # This class provides a set of default CRUD operations for the `Task` model.
    # Specifies the serializer to be used for converting `Task` instances to JSON and vice versa.
    serializer_class = TaskSerializer
    
    # Ensures that only authenticated users can access this viewset
    permission_classes = [permissions.IsAuthenticated]

    # Overrides the default `get_queryset` method to return only tasks associated
    # with the currently authenticated user
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    # Overrides the `perform_create` method to automatically set the `user` field to
    # the currently authenticated user when a new task is created
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # Specifies the filtering and ordering backends to be used.
    # `DjangoFilterBackend` allows for field-based filtering, and `fiters.OrderingFilter`
    # allows for ordering of results
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]

    # Defines the fields that can be used for filtering tasks. 
    # Here, tasks can be filtered by `priority` and `due_date`
    filterset_fields = ['priority', 'due_date']

    # Specifies the fields that can be used for ordering the results. 
    # Here, tasks can be ordered by `due_date`
    ordering_fields = ['due_date']
