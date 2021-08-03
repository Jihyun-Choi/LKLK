from django.urls import path

from teamapp.views import TeamView

app_name = "teamapp"

urlpatterns = [
    path('team/', TeamView.as_view(), name='team')
]