from django.contrib.auth.models import User
from django.db import models

class Project(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='project', null=True)

    title = models.CharField(max_length=200, null=False)#제목이 꼭 있도록 null=False
    image = models.ImageField(upload_to='project/', null=False)
    image2 = models.ImageField(upload_to='project/', null=False)
    image3 = models.ImageField(upload_to='project/', null=False)

    content = models.TextField(null=True)#내용도 꼭 있도록 null=False

    PERSON_CHOICES = [('1', '1명'), ('2', '2명'), ('3', '3명'), ('4', '4명'), ('5', '5명'), ('6', '6명')]
    personnel = models.CharField(max_length=2, choices=PERSON_CHOICES, default='1')

    created_at = models.DateField(auto_now_add=True, null=True)

    count = models.IntegerField(default=0)