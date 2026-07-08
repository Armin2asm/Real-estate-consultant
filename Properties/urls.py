from django.urls import path,include

from .views import AddPropertyView, PropertyDetailView, PropertyListView,PropertyUpdateView,PropertyDeleteView



app_name = "properties"

urlpatterns = [

    path("add/", AddPropertyView.as_view(), name="add_property"),
    path("<int:pk>/", PropertyDetailView.as_view(), name="property_detail"),
    path("", PropertyListView.as_view(), name="property_list"),
    path("<int:pk>/edit/", PropertyUpdateView.as_view(), name="edit_property"),
    path("<int:pk>/delete/", PropertyDeleteView.as_view(), name="delete_property"),


]
