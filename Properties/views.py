from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Property,PropertyImage
from django.shortcuts import redirect
from django.views.generic import DetailView
from django.views.generic import ListView
from .forms import PropertyForm
class AddPropertyView(CreateView):
    model = Property
    form_class = PropertyForm
    template_name = "properties/add_property.html"

    def form_valid(self, form):
        property = form.save(commit=False)

        property.owner = self.request.user
        property.save()

        images = self.request.FILES.getlist("images")

        for image in images:
            PropertyImage.objects.create(
                property=property,
                image=image
            )

        return redirect("Home")
        


class PropertyDetailView(DetailView):
    model = Property
    template_name = "properties/property_detail.html"
    context_object_name = "property"
    

class PropertyListView(ListView):
    model = Property
    template_name = "properties/property_list.html"
    context_object_name = "properties"
    
    
class PropertyUpdateView(LoginRequiredMixin, UpdateView):
    model = Property
    form_class = PropertyForm
    template_name = "properties/edit_property.html"
    success_url = reverse_lazy("properties:property_list")

    def get_queryset(self):
        return Property.objects.filter(owner=self.request.user)
    
class PropertyDeleteView(LoginRequiredMixin, DeleteView):
    model = Property
    template_name = "properties/delete_property.html"
    success_url = reverse_lazy("properties:property_list")

    def get_queryset(self):
        return Property.objects.filter(owner=self.request.user)