from django import forms
from .models import AgentsName


class AgentForm(forms.ModelForm):
    class Meta:
        model = AgentsName
        fields = "__all__"