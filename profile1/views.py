from django.db.models.signals import post_init
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ProfileForm
from django.contrib.auth.models import User
#from apps.profile1.models import Profile
from .models import Profile
from django.views.generic.base import TemplateView
# Create your views here.

class ProfileView(LoginRequiredMixin, TemplateView):
    profile_form = ProfileForm
    template_name = 'profile.html'
        
    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None

        profile_form = ProfileForm(post_data,file_data, instance = request.user.profile)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return HttpResponseRedirect(reverse_lazy('profile'))
        context = self.get_context_data(
            profile_form = profile_form
        )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

"""class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    profile_form = ProfileForm
    template_name = 'profile-update.html'

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None

        profile_form = ProfileForm(post_data,file_data, instance = request.user.profile)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return HttpResponseRedirect(reverse_lazy('profile'))
        context = self.get_context_data(
            profile_form = profile_form
        )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
        """
