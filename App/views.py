from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import datetime
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
import httpagentparser
import os, sys


def GetRemotePCIP(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def BrowserDetails(request):
    agent = request.environ.get('HTTP_USER_AGENT')
    browser = httpagentparser.detect(agent)
    if not browser:
        browser = agent.split('/')[0]
    else:
        browser_name = browser['browser']['name'] 
        browser_version = browser['browser']['version']
        browser = browser_name + " " + browser_version
    return browser


def StudentList(request, slug):
    try:
        batch_id = int(slug)
        batch = Batch.objects.get(id=batch_id)
        student = Student.objects.filter(batch__id=batch_id)
        context = {
            'student': student, 'batch': batch
        }
        return render(request, 'App/student.html', context=context)
    except:
        return redirect('/404/')


def BatchList(request):
    try:
        batch = Batch.objects.all().filter(is_active=True)
        context = {
            'batch': batch
        }
        return render(request, 'App/batches.html', context=context)
    except:
        return redirect('/404/')


def CompletedBatchList(request):
    try:
        batch = Batch.objects.all().filter(is_active=False)
        context = {
            'batch': batch
        }
        return render(request, 'App/completed.html', context=context)
    except:
        return redirect('/404/')


def Feedback(request):
    try:
        feedback = FeedBack.objects.filter(is_active=True).order_by('-created_at')
        context = {
            'feedback': feedback
        }
        return render(request, 'App/feedback.html', context=context)
    except:
        return redirect('/404/')


def SubmitFeedback(request):
    try:
        if request.method == 'GET':
            context = {}
            return render(request, 'App/submit_feedback.html', context=context)
        else:
            try:
                name = request.POST['fullname']
                course = request.POST['course']
                message = request.POST['subject']
                country = request.POST['country']
                ip = GetRemotePCIP(request)
                browser = BrowserDetails(request)
                
                pre_feedback = FeedBack.objects.filter(
                    ip=ip, browser=browser
                )
                if len(pre_feedback) == 0:
                    o = FeedBack(
                        name=name, course=course, message=message, country=country, ip=ip, browser=browser
                    )
                    o.save()
                else:
                    request.method = 'GET'
                    context = {'status': 0}
                    return render(request, 'App/submit_feedback.html', context=context)
                
                return redirect('/feedback/')
            except Exception as e:
                print(e)
                return redirect('/submit-feedback/')
    except:
        return redirect('/404/')


def Notice(request, slug):
    try:
        id = int(slug)
        batch = Batch.objects.get(id=id)
        context = {
            'batch': batch
        }
        return render(request, 'App/notice.html', context=context)
    
    except Exception as e:
        return redirect('/404/')

def NotFound(request):
    return render(request, 'App/404.html')
