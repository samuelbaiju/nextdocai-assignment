from celery import shared_task
from datetime import datetime
from management.models import DevelopmentTask, DesignTask

@shared_task
def check_overdue_tasks():
    now = datetime.now()
    overdue_tasks_dev = DevelopmentTask.objects.filter(
        due_date__lt=now, status__in=['pending', 'in_progress']
    )
    overdue_tasks_design = DesignTask.objects.filter(
        due_date__lt=now, status__in=['pending', 'in_progress']
    )
    
    # Update statuses
    overdue_tasks_dev.update(status='overdue')
    overdue_tasks_design.update(status='overdue')

    # Send notifications (e.g., via email, but for this example, a simple print is fine)
    print(f"Marked {overdue_tasks_dev.count()} development tasks as overdue.")
    print(f"Marked {overdue_tasks_design.count()} design tasks as overdue.")