from django.shortcuts import render, redirect
from backend.models import *
from datetime import datetime
import smtplib
import math
import random

context = dict()


def home(request):
    context['msg'] = ''
    context['videos'] = Video.objects.all().order_by('-upload_time')
    return render(request, 'index.html', context)


def login(request):
    context['msg'] = ''
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


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


def sendOTP(OTP):
    email_sender = 'riaduttademo@gmail.com'
    email_password = 'wokvndvsrmufesgz'
    email_receiver = user.email

    subject = 'Reset Password'
    body = "The OTP for reseting your password is " + OTP

    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(email_sender, email_password)
    s.sendmail(email_sender, email_receiver, body)
    s.quit()


def register(request):
    context['msg'] = ''
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if User.objects.filter(email=email):
            context['msg'] = "Already registered email! Try with new one."
        else:
            if password == cpassword:
                OTP = generateOTP()
                sendOTP(OTP)

                user = User.objects.create(
                    fullname=fullname,
                    email=email,
                    password=password,
                )
                user.save()
                request.session['user'] = email
                context['msg'] = "Email registered. Successfully logged in!"
                return render(request, 'index.html', context)
            else:
                context['msg'] = "Passwords not matched. Try again!"

    return render(request, 'register.html', context)


def logout(request):
    request.session['user'] = ''
    context['videos'] = Video.objects.all().order_by('-upload_time')
    context['msg'] = "Successfully logged out!"
    return render(request, 'index.html', context)


def admin_panel(request):
    context['msg'] = ''
    if request.session.get('user') == 'plugnplay150523@gmail.com':
        context['users'] = User.objects.all().order_by('create_time')
        context['videos'] = Video.objects.all().order_by('-upload_time')
        return render(request, 'admin-panel.html', context)
    else:
        context['msg'] = "You do not have access!"
    return render(request, 'index.html', context)


def upload_video(request):
    context['msg'] = ''
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


def edit_video(request, id):
    context['msg'] = ''
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

    return render(request, 'edit-video.html', context)


def delete_video(request, id):
    video = Video.objects.get(id=id)
    video.delete()

    context['msg'] = "Successfully video deleted."
    context['videos'] = Video.objects.all().order_by('-upload_time')

    return render(request, 'admin-panel.html', context)
