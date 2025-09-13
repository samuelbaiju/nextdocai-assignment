from rest_framework import serializers
from .models import Project, DevelopmentTask, DesignTask

class DevelopmentTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevelopmentTask
        fields = '__all__'

class DesignTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignTask
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'tasks']

    def get_tasks(self, obj):
        # Fetch tasks using the new related_names
        tasks = list(obj.developmenttask_tasks.all()) + list(obj.designtask_tasks.all())
        # Sort tasks by due date or another field if needed
        return [
            {
                'type': 'Development',
                'id': task.id,
                'title': task.title,
                'status': task.status,
                'due_date': task.due_date,
            }
            for task in tasks
        ]