from django.db import models
from task.models import TaskModel

# Create your models here.

class TaskCategory(models.Model):
    categoryName = models.CharField(max_length=100, verbose_name='Category Name')
    taskModel = models.ForeignKey(TaskModel, on_delete=models.CASCADE, verbose_name='Task Name')
    
    def __str__(self) -> str:
        return self.categoryName