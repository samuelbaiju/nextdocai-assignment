from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from datetime import timedelta
from django.utils import timezone
from .models import Project, DevelopmentTask, DesignTask
from .tasks import check_overdue_tasks

class ProjectAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.project = Project.objects.create(name='Test Project', description='A test project.')
        self.list_url = reverse('project-list')
        self.detail_url = reverse('project-detail', args=[self.project.id])

    def test_project_creation(self):
        response = self.client.post(self.list_url, {'name': 'New Project', 'description': 'Description.'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Project.objects.count(), 2)

    def test_project_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

class TaskSignalsTest(TestCase):
    def test_task_creation_signal(self):
        with self.assertLogs('root', level='INFO') as cm:
            Project.objects.create(name='Signal Test Project')
            DevelopmentTask.objects.create(
                project=Project.objects.first(),
                title='Signal Task',
                due_date=timezone.now() + timedelta(days=1)
            )
        self.assertIn("New task created: 'Signal Task' for project 'Signal Test Project'", cm.output[0])

class CeleryTasksTest(TestCase):
    def test_overdue_tasks(self):
        project = Project.objects.create(name='Overdue Test Project')
        # Create an overdue task
        overdue_task = DevelopmentTask.objects.create(
            project=project,
            title='Overdue Task',
            due_date=timezone.now() - timedelta(days=1),
            status='pending'
        )
        # Run the celery task
        check_overdue_tasks.delay()
        overdue_task.refresh_from_db()
        self.assertEqual(overdue_task.status, 'overdue')