from django.db import models

# Create your models here.
class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=100, verbose_name='Task Title')
    taskDescription = models.TextField(verbose_name='Task Description')
    isCompleted = models.BooleanField(default=False, verbose_name='Task Completed?')
    taskAssignDate = models.DateField(verbose_name='Task Assign Date')
    
    def __str__(self) -> str:
        return self.taskTitle