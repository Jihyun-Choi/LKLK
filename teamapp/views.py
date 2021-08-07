from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from joinapp.models import Join
from projectapp.models import Project
from teamapp.models import Team


@method_decorator(login_required, 'get')
class TeamView(RedirectView):

    #projectapp의 detail에서 team버튼을 누르므로 detail의 pk를 넘겨받아 버튼을 누르면 다시 그 페이지로로
    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):
        #전달받은 pk를 이용해 user, project객체를 특정하고 이를 필터링하는데 사용
        user = get_object_or_404(User, pk=self.request.GET.get('user'))
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        join = Join.objects.filter(user=user, project=project)

        if join.exists():
            join.delete()


        #필터링 된 팀 객체를 변수에 받아옴
        team = Team.objects.filter(user=project.writer, project=project)

        #user, project에 맞는 team객체가 없다면 새로 생성
        if not(team.exists()):
            Team(user=project.writer, project=project).save()


        for object in team:
            #if object.project.title == project.title:
                if object.member1 == None:
                    object.member1 = user
                elif object.member2 == None:
                    object.member2 = user
                elif object.member3 == None:
                    object.member3 = user
                elif object.member4 == None:
                    object.member4 = user
                elif object.member5 == None:
                    object.member5 = user
                else:
                    pass
                #elif object.member3 == None:
                #    object.member3 = user
                #elif object.member4 == None:
                #    object.member4 = user
                #elif object.member5 == None:
                #    object.member5 = user

                object.save()

        return super(TeamView, self).get(request, *args, **kwargs)