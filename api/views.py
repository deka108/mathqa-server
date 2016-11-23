"""
# Name:           cms/urls.py
# Description:
# Created by:     Phuc Le-Sanh
# Date Created:   Nov 23, 2016
# Last Modified:  Nov 23, 2016
# Modified by:    Phuc Le-Sanh
"""
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
# from django.core import serializers

from meas_models.models import *


# Topic
def topic_index(request):
    if request.method == 'GET':
        results = [topic.as_json() for topic in Topic.objects.all()]
        return HttpResponse(
            json.dumps(results),
            content_type="application/json"
        )

    return __error_response


@csrf_exempt
def topic_post(request):
    if request.method == 'POST':
        topic = Topic(name=request.POST.__getitem__('name'),
                      order=request.POST.__getitem__('order'),
                      description=request.POST.__getitem__(
            'description'),
            subject=Subject.objects.get(
            pk=request.POST.__getitem__('subject'))
        )
        topic.save()

        if topic.pk is not None:
            return HttpResponse(
                json.dumps([topic.as_json()]),
                content_type="application/json"
            )

    return __error_response


def topic_put(request):
    return


def topic_delete(request):
    return


# Concept
def concept_index(request):
    return


def concept_post(request):
    return


def concept_put(request):
    return


def concept_delete(request):
    return


# Paper
def paper_index(request):
    return


def paper_post(request):
    return


def paper_put(request):
    return


def paper_delete(request):
    return


def __error_response():
    return HttpResponse(
        json.dumps({"Error"}),
        content_type="application/json"
    )
