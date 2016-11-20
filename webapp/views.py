from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from meas_models.models import *


def custom_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        if user.is_superuser:
            return redirect('/cms/topic')
        else:
            return redirect('/')
    else:
        return redirect('/login/')


def dashboard_index(request):
    if not request.user.is_authenticated:
        return redirect('/login/')

    return render(request, 'webapp/dashboard/index.html',
                  __user_info(request, {}))


def topic_index(request):
    if not request.user.is_authenticated:
        return redirect('/login/')

    return render(request, 'webapp/topic/index.html', __user_info(request, {
        "topics": Topic.objects.all
    }))


def topic_detail(request, topic_id):
    if not request.user.is_authenticated:
        return redirect('/login/')

    topic = Topic.objects.get(pk=topic_id)

    return render(request, 'webapp/topic/index.html', __user_info(request, {
        "topics": Topic.objects.all,
        "concepts": topic.concept_set.all,
        "current_topic": topic
    }))


def topic_concept(request, topic_id, concept_id):
    if not request.user.is_authenticated:
        return redirect('/login/')

    topic = Topic.objects.get(pk=topic_id)
    concept = Concept.objects.get(pk=concept_id)
    keypoints = concept.keypoint_set.all()

    return render(request, 'webapp/topic/concept.html', __user_info(request, {
        "topics": Topic.objects.all,
        "concepts": topic.concept_set.all,
        "current_topic": topic,
        "current_concept": concept,
        "keypoints": keypoints
    }))


def adaptive_index(request):
    if not request.user.is_authenticated:
        return redirect('/login/')

    return render(request, 'webapp/adaptive_test/index.html',
                  __user_info(request, {}))


def contest_index(request):
    if not request.user.is_authenticated:
        return redirect('/login/')

    return render(request, 'webapp/contest/index.html',
                  __user_info(request, {}))


def __user_info(request, updated_list=""):
    result = {
        'is_authenticated': request.user.is_authenticated,
        'current_user': request.user
    }

    if any(updated_list):
        result.update(updated_list)

    return result
