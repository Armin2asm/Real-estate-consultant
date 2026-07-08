from django import forms
from .models import Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = "__all__"

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),

            "property_type": forms.Select(attrs={"class": "form-select"}),

            "transaction_type": forms.Select(attrs={"class": "form-select"}),

            "owner_name": forms.TextInput(attrs={"class": "form-control"}),

            "owner_phone": forms.TextInput(attrs={"class": "form-control"}),

            "city": forms.TextInput(attrs={"class": "form-control"}),

            "address": forms.Textarea(
                attrs={"class": "form-control", "rows": 3}
            ),

            "area": forms.NumberInput(attrs={"class": "form-control"}),

            "bedrooms": forms.NumberInput(attrs={"class": "form-control"}),

            "bathrooms": forms.NumberInput(attrs={"class": "form-control"}),

            "floor": forms.NumberInput(attrs={"class": "form-control"}),

            "year_built": forms.NumberInput(attrs={"class": "form-control"}),

            "sale_price": forms.NumberInput(attrs={"class": "form-control"}),

            "mortgage_price": forms.NumberInput(attrs={"class": "form-control"}),

            "rent_price": forms.NumberInput(attrs={"class": "form-control"}),

            "description": forms.Textarea(
                attrs={"class": "form-control", "rows": 5}
            ),

            "parking": forms.CheckboxInput(attrs={"class": "form-check-input"}),

            "elevator": forms.CheckboxInput(attrs={"class": "form-check-input"}),

            "storage_room": forms.CheckboxInput(attrs={"class": "form-check-input"}),

            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }