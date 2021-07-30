from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from joinapp.models import Join
from projectapp.models import Project


@method_decorator(login_required, 'get')
class JoinView(RedirectView):

    #projectapp의 detail에서 join버튼을 누르므로 detail의 pk를 넘겨받아 버튼을 누르면 다시 그 페이지로로
    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user
        join = Join.objects.filter(user=user, project=project)

        if join.exists():
            join.delete()
            project.count -= 1
        else:
            Join(user=user, project=project).save()
            project.count += 1

        project.save()
        return super(JoinView, self).get(request, *args, **kwargs)