from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Project(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Task(BaseModel):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('overdue', 'Overdue'),
    )
    # The %(class)s_tasks syntax dynamically creates a unique related_name
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='%(class)s_tasks'
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    due_date = models.DateTimeField()

    class Meta:
        abstract = True

class DevelopmentTask(Task):
    developer = models.CharField(max_length=255)

class DesignTask(Task):
    designer = models.CharField(max_length=255)