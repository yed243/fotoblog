from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PhotoForm
from .models import Blog, Photo

# Create your views here.
@login_required
def home(request):
    photo = Photo.objects.all()
    return render(request, 'blog/home.html', context={'photos': photo})

@login_required
def photo_upload(request):
    form = PhotoForm()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect('home')
    else:
        form = PhotoForm()
    return render(request, 'blog/photo_upload.html', {'form': form})