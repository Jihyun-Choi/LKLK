from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Team(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='team')

    # member를 다룰 수 있는 자료형으로 반복문 돌릴 수 있도록
    member1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team')
    member2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team')
    member3 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team')
    member4 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team')
    member5 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team')
    fail = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team')


    # 하나의 user가 프로젝트를 한번만 team할 수 있도록
    class Meta:
        unique_together = ('user', 'project')