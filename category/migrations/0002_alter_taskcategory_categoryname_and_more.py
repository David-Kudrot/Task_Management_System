# Generated by Django 5.0 on 2023-12-08 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('task', '0002_alter_taskmodel_iscompleted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcategory',
            name='categoryName',
            field=models.CharField(max_length=100, verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='taskcategory',
            name='taskModel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.taskmodel', verbose_name='Task Name'),
        ),
    ]
