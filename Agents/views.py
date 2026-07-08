from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect

from .models import AgentsName
from .forms import AgentForm


class AgentsView(ListView):
    model = AgentsName
    template_name = "Agents/index1.html"
    context_object_name = "agents"


class AddAgentView(CreateView):
    model = AgentsName
    form_class = AgentForm
    template_name = "Agents/add_agent.html"

    def form_valid(self, form):
        form.save()
        return redirect("Home")