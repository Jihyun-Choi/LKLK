from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Join(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='join')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='join')

    # 하나의 user가 프로젝트를 한번만 join할 수 있도록
    class Meta:
        unique_together = ('user', 'project')
