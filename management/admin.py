from django.contrib import admin
from .models import Project, DevelopmentTask, DesignTask

class DevelopmentTaskInline(admin.TabularInline):
    model = DevelopmentTask
    extra = 1

class DesignTaskInline(admin.TabularInline):
    model = DesignTask
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name']
    list_filter = ['created_at']
    inlines = [DevelopmentTaskInline, DesignTaskInline]
    actions = ['mark_as_complete']

    def mark_as_complete(self, request, queryset):
        for project in queryset:
            project.developmenttask_tasks.all().update(status='completed')
            project.designtask_tasks.all().update(status='completed')
        self.message_user(request, f"Marked tasks for {queryset.count()} projects as completed.")
    mark_as_complete.short_description = "Mark selected projects' tasks as completed"