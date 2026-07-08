from django.views.generic import ListView


from .models import HomePage
from Properties.models import Property
from Agents.models import AgentsName


class HomeView(ListView):
    model = HomePage
    template_name = "HomePage/index1.html"
    context_object_name = "homepage"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["property_list"] = (
            Property.objects.filter(is_active=True)
            .order_by("-created_at")[:3]
        )

        context["agents"] = AgentsName.objects.order_by("-id")[:3]
        return context