from django.db import models
from django.contrib.auth.models import User # User model will be used to associate tasks with users

# Create your models here.
class Task(models.Model): # Task Model
    STATUS_CHOICES = [ # Possible statuses for a task
        ('pending', 'Pending'), # (stored in the db, human-readable name)
        ('in progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    PRIORITY_CHOICES = [ # A list of tuples defining the possible priorities for a task
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    # Fields
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateField(null=True, blank=True) # Optional

    # A `ForeignKey` that creates a many-to-one relationship with the `User` model.
    # This means each task is associated with a user, and each user can have multiple
    # tasks.
    # The `related_name="tasks"` allows you to access a user's tasks using `user.tasks`.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

    # This method returns the title of the task.
    # It's used to provide a human-readable representation of the model instance,
    # which is useful in Django's admin interface and when printing instances.
    def __str__(self):
        return self.title
