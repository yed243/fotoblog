from django.shortcuts import render, redirect
#from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import View
from .forms import SignUpForm
from .forms import UploadProfilePhotoForm

# Create your views here.
"""def login_view(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('home')
                
            else:
                message = 'Identifiants invalides.'

    return render(request, 'authentication/login.html', context={'form': form, 'message': message})
"""
##########################################################
"""
def logout_user(request):
    logout(request)
    return(redirect('login'))
"""
###################################################################
"""
# utilisation de View base sur les classes
class LoginView(View):
    template_name = 'authentication/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('home')
                
            else:
                message = 'Identifiants invalides.'
        return render(request, self.template_name, context={'form': form, 'message': message})
"""

def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Votre compte a été créé avec succès. Vous pouvez maintenant vous connecter.')
            login(request, user)
            return redirect('login')
    return render(request, 'authentication/signup.html', context={'form': form})

def upload_profile_photo(request):
    form = UploadProfilePhotoForm(instance=request.user)
    if request.method == 'POST':
        form = UploadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre photo de profil a été mise à jour avec succès.')
            return redirect('home')
    else:
        form = UploadProfilePhotoForm(instance=request.user)
    return render(request, 'authentication/upload_profile_photo.html', {'form': form})