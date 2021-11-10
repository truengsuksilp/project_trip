from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Auth
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

class SignUp(View):
    def get(self, request):
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'signup.html', context)

    def post(self, request):
        form = SignUpForm(request.POST)
        birth_date = request.POST.get('birth_date')

        if form.is_valid():
            user=form.save()
            profile = Profile.objects.create(user=user, birth_day=birth_day)
            
            # Authenticate
            # username = form.
            # cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=password)

            login(request, user)
            return redirect('home')
        else: 
            context = {'form': form}
            return render(request,'signup.html', context)