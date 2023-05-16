from django.shortcuts import render, redirect, HttpResponse
from backend.models import *
from datetime import datetime
import smtplib
from email.message import EmailMessage
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


def sendOTP(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    cpassword = request.POST.get('cpassword')

    if User.objects.filter(email=email):
        return HttpResponse(-1)
    else:
        if password == cpassword:
            OTP = generateOTP()

            email_sender = 'plugnplay150523@gmail.com'
            email_password = 'ljaxtrrnbqvhmdqw'

            message = EmailMessage()
            message['Reply-to'] = email_sender
            message['From'] = email_sender
            message['To'] = email
            message['Subject'] = 'Email Verification'

            message.set_content("The OTP for verifing your email is " + OTP)
            s = smtplib.SMTP_SSL('smtp.gmail.com', 465)

            try:
                s.login(email_sender, email_password)
                s.sendmail(email_sender, email, message.as_string())
                s.quit()
            except Exception as e:
                print('Email: ', e)

            return HttpResponse(OTP)
        else:
            return HttpResponse(-2)


def confirmOTP(request):
    otp = request.POST.get("otp")
    otp_gen = request.POST.get("otp_gen")

    if otp == otp_gen:
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create(
            fullname=fullname,
            email=email,
            password=password,
        )
        user.save()

        return HttpResponse(1)
    else:
        return HttpResponse(0)


def register(request):
    return render(request, 'register.html')


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
