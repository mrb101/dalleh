from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

from .forms import ContactUsForm


class HomeView(View):
    template_name = 'pages/home.html'

    def get(self, request, *args, **kwargs):
        context = {'form': ContactUsForm()}
        return render(request, self.template_name, context)


class AboutView(View):
    template_name = 'pages/about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context)


class ServicesView(View):
    template_name = 'pages/services.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class ContactView(View):
    template_name = 'pages/contact.html'
    success_message = 'Your message has been sent!'
    error_message = 'You have entered invalid information. check the errors!!'

    def get(self, request, *args, **kwargs):
        context = {'form': ContactUsForm()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ContactUsForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            # Do Something with form data
            messages.success(request, self.success_message)
            return redirect("pages:contact_us")
        else:
            messages.error(request, self.error_message)
            return render(request, self.template_name, contaxt)
