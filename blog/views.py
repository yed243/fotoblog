from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BlogForm, PhotoForm
from .models import Blog, Photo

# Create your views here.
@login_required
def home(request):
    photo = Photo.objects.all()
    blog = Blog.objects.all()
    return render(request, 'blog/home.html', context={'photos': photo, 'blogs': blog})

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

@login_required
def blog_and_photo_upload(request):
    photo_form = PhotoForm()
    blog_form = BlogForm()
    if request.method == 'POST':
        blog_form = BlogForm(request.POST)
        photo_form = PhotoForm(request.POST, request.FILES)
        if all([blog_form.is_valid(), photo_form.is_valid()]):
            blog = blog_form.save(commit=False)
            blog.author = request.user
            blog.save()

            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect('home')

    context = {
        'blog_form': blog_form,
        'photo_form': photo_form
    }
    return render(request, 'blog/create_blog_post.html', context)

@login_required
def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog/view_blog.html', {'blog': blog})