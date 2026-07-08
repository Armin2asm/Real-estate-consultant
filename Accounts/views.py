from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Contact
from .forms import ContactForm
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'Accounts/contact.html'
    success_url = reverse_lazy('Home')

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "Accounts/signup.html"
    success_url = reverse_lazy("account:login")