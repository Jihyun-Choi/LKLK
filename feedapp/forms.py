from django.forms import ModelForm

from feedapp.models import Feed


class FeedCreationForm(ModelForm):
    class Meta:
        model = Feed
        fields = ['title',  'content']