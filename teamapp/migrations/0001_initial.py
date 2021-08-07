# Generated by Django 3.2.5 on 2021-08-07 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projectapp', '0003_project_count'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_1', to=settings.AUTH_USER_MODEL)),
                ('member2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_2', to=settings.AUTH_USER_MODEL)),
                ('member3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_3', to=settings.AUTH_USER_MODEL)),
                ('member4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_4', to=settings.AUTH_USER_MODEL)),
                ('member5', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_5', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='projectapp.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'project')},
            },
        ),
    ]
