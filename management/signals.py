from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import DevelopmentTask, DesignTask, Project

@receiver(post_save, sender=DevelopmentTask)
@receiver(post_save, sender=DesignTask)
def notify_on_task_creation(sender, instance, created, **kwargs):
    if created:
        print(f"New task created: '{instance.title}' for project '{instance.project.name}'.")

@receiver(post_delete, sender=Project)
def cascade_delete_tasks(sender, instance, **kwargs):
    # Tasks are automatically cascade-deleted due to the ForeignKey on_delete=models.CASCADE
    print(f"Project '{instance.name}' was deleted. All associated tasks have also been removed.")