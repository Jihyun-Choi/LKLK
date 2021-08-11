from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView

from commentapp.decorators import comment_ownership_required
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment
from feedapp.models import Feed
from projectapp.models import Project
from teamapp.models import Team


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'
    context_object_name = 'target_comment'

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.project = Project.objects.get(pk=self.request.POST['project_pk'])
        temp_comment.feed = Feed.objects.get(pk=self.request.POST['feed_pk'])
        temp_comment.writer = self.request.user
        temp_comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.request.POST['project_pk']})


# class CommentDetailView(DetailView):
#     model = Comment
#     template_name = 'commentapp/detail.html'
#     context_object_name = 'comment'
#     def get_context_data(self, **kwargs):
#         project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
#         comment = Comment.object.filter(project=project)
#         team = Team.objects.all()
#         return super(CommentDetailView, self).get_context_data(comment=comment, team=team, project=project, **kwargs)

class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    #success_url = reverse_lazy('commentapp:list')
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return reverse('home')
# class CommentListView(ListView):
#     model = Comment
#     context_object_name = 'comment_list'
#     template_name = 'commentapp/list.html'
#     paginate_by = 25
#