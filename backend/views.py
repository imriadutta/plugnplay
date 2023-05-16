from django.shortcuts import render, redirect
from backend.models import *
from datetime import datetime

context = {
    'users': User.objects.all().order_by('create_time'),
    'videos': Video.objects.all().order_by('-upload_time'),
    'msg': '',
}


def context_update(func):
    def modified_func(*args, **kwargs):
        context = {
            'users': User.objects.all().order_by('create_time'),
            'videos': Video.objects.all().order_by('-upload_time'),
            'msg': '',
        }
        return func(*args, **kwargs)
    return modified_func


@context_update
def home(request):
    return render(request, 'index.html', context)


@context_update
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email)
        if user:
            if user.last().password == password:
                request.session['user'] = email
                context['msg'] = "Successfully logged in!"
                return render(request, 'index.html', context)
            else:
                context['msg'] = "Wrong password. Try again!"
        else:
            context['msg'] = "No email exist!"

    return render(request, 'login.html', context)


@context_update
def register(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if User.objects.filter(email=email):
            context['msg'] = "Already registered email! Try with new one."
        else:
            if password == cpassword:
                user = User.objects.create(
                    fullname=fullname,
                    email=email,
                    password=password
                )
                user.save()
                request.session['user'] = email
                context['msg'] = "Email registered. Successfully logged in!"
                return render(request, 'index.html', context)
            else:
                context['msg'] = "Passwords not matched. Try again!"

    return render(request, 'register.html', context)


@context_update
def logout(request):
    request.session['user'] = ''
    context['msg'] = "Successfully logged out!"
    return render(request, 'index.html', context)


@context_update
def admin_panel(request):
    if request.session.get('user') == 'plugnplay150523@gmail.com':
        return render(request, 'admin-panel.html', context)
    else:
        context['msg'] = "You do not have access!"
        return render(request, 'index.html', context)


@context_update
def upload_video(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        content = request.POST.get('content')

        video = Video.objects.create(
            title=title,
            description=description,
            content=content,
        )
        video.save()

        context['msg'] = "Successfully video uploaded."

    return render(request, 'upload-video.html', context)


@context_update
def edit_video(request, id):
    video = Video.objects.get(id=id)
    context['video'] = video

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        content = request.POST.get('content')

        if title != '':
            video.title = title
        if description != '':
            video.description = description
        if content != '':
            video.content = content

        video.save()

        context['msg'] = "Successfully video updated."
        context['videos'] = Video.objects.all().order_by('-upload_time')

    return render(request, 'edit-video.html', context)


@context_update
def delete_video(request, id):
    video = Video.objects.get(id=id)
    video.delete()

    context['msg'] = "Successfully video deleted."
    context['videos'] = Video.objects.all().order_by('-upload_time')

    return render(request, 'admin-panel.html', context)
