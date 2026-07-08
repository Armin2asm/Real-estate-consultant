from django.urls import path
from .views import AgentsView, AddAgentView

app_name = "agents"

urlpatterns = [
    path("", AgentsView.as_view(), name="agents"),
    path("add/", AddAgentView.as_view(), name="add_agent"),
]