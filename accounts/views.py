from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User

from .models import UserProfile
from .forms import UserProfileForm


class MyProfileDetailView(View):
    template_name = 'accounts/show.html'

    def get_user(self):
        """
        returns -> Object: User
        """
        return User.objects.get(username=self.request.user.username)

    def get(self, request, *args, **kwargs):
        context = {'user': self.get_user()}
        return render(request, self.template_name, context)


class MyProfileFormView(View):
    template_name = 'accounts/form.html'
    success_message = 'Your Profile has been updated!'
    error_message = 'You have entered invalid information, Check Errors'

    def get_user(self):
        """
        returns -> Object: User
        """
        return User.objects.get(username=self.request.user.username)

    def get(self, request, *args, **kwargs):
        context = {'form': UserProfileForm(instance=self.get_user().profile)}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UserProfileForm(request.POST, instance=self.get_user().profile)
        context = {
            'form': form
        }
        if form.is_valid():
            user_profile = form.save()
            messages.success(request, self.success_message)
            return redirect("accounts:profile_details")
        else:
            messages.error(request, self.error_message)
            return render(request, self.template_name, context)
