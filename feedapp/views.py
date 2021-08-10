from django.contrib.auth.decorators import login_required

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView

from feedapp.decorators import feed_ownership_required
from feedapp.forms import FeedCreationForm
from feedapp.models import Feed
from joinapp.models import Join
from projectapp.models import Project
from teamapp.models import Team


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class FeedCreateView(CreateView):
    model = Feed
    form_class = FeedCreationForm
    template_name = 'feedapp/create.html'

    def form_valid(self, form):
        temp_post = form.save(commit=False)
        temp_post.writer = self.request.user
        temp_post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('feedapp:detail', kwargs={'pk': self.object.pk})

class FeedDetailView(DetailView):
    model = Feed
    context_object_name = 'target_post'
    template_name = 'feedapp/detail.html'

    def get_context_data(self, **kwargs):
        project = self.object
        team = Team.objects.filter(user=project.writer, project=project)

        return super(FeedDetailView, self).get_context_data(team=team, **kwargs)

@method_decorator(feed_ownership_required, 'get')
@method_decorator(feed_ownership_required, 'post')
class FeedUpdateView(UpdateView):
    model = Feed
    context_object_name = 'target_post'
    form_class = FeedCreationForm
    template_name = 'feedapp/update.html'

    def get_success_url(self):
        return reverse('feedapp:detail', kwargs={'pk': self.object.pk})

@method_decorator(feed_ownership_required, 'get')
@method_decorator(feed_ownership_required, 'post')
class FeedDeleteView(DeleteView):
    model = Feed
    context_object_name = 'target_post'
    success_url = reverse_lazy('feedapp:list')
    template_name = 'feedapp/delete.html'

class FeedListView(ListView):
    model = Feed
    context_object_name = 'post_list'
    template_name = 'feedapp/list.html'
    paginate_by = 25

    # def get(self, request):
    #     from django.shortcuts import render
    #
    #     if request.method == 'GET':
    #         project_name = request.GET.get('project_name')
    #         data = {'project_name':project_name,}
    #         return render(request, "feedapp/list.html",data)
    #     else:
    #         return render(request, "feedapp/list.html",{})

    #def get(self, request):
    #    from django.shortcuts import render
    #    team_list = Team.objects.all()
    #    if request.method == 'GET':
    #        project_name = request.GET.get('project_name')
    #        data = {'project_name':project_name,'join_list':join_list}
    #    else:
    #        data = {'join_list':join_list}
    #    return render(request, "feedapp/list.html", data)

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        team = Team.objects.filter(user=project.writer, project=project)
        if not(team.exists()):
            team = None

        return super(FeedListView, self).get(request, *args, **kwargs, team=team, project=project)


    # def get_context_data(self, **kwargs):
    #     join_list = Join.objects.all()
    #     return super(FeedListView, self).get_context_data(join_list=join_list, **kwargs)