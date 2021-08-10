from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Feed(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='feed', null=True)

    title = models.CharField(max_length=200, null=True)

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='feed', null=True)
    image = models.ImageField(upload_to='feed/', null=False)
    content = RichTextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)