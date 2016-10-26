from django.shortcuts import render

from meas_models.models import *


def dashboard_index(request):
    return render(request, 'webapp/dashboard/index.html',
                  __user_info(request, {}))


def topic_index(request):
    return render(request, 'webapp/topic/index.html', __user_info(request, {
        "topics": Topic.objects.all
    }))


def topic_concept(request, topic_id, concept_id):
    topic = Topic.objects.get(pk=topic_id)
    concept = Concept.objects.get(pk=concept_id)
    return render(request, 'webapp/topic/concept.html', __user_info(request, {
        "topics": Topic.objects.all,
        "concepts": topic.concept_set.all,
        "current_topic": topic,
        "current_concept": concept
    }))


def adaptive_index(request):
    return render(request, 'webapp/adaptive_test/index.html',
                  __user_info(request, {}))


def contest_index(request):
    return render(request, 'webapp/contest/index.html',
                  __user_info(request, {}))


def __user_info(request, updated_list):
    result = {
        'is_authenticated': request.user.is_authenticated,
        'current_user': request.user
    }

    if any(updated_list):
        result.update(updated_list)

    return result
