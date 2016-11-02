from django.shortcuts import render

from meas_models.models import *


def dashboard_index(request):
    return render(request, 'cms/topic/index.html', __user_info(request, {
        "topics": Topic.objects.all
    }))


def __user_info(request, updated_list=""):
    result = {
        'is_authenticated': request.user.is_authenticated,
        'current_user': request.user
    }

    if any(updated_list):
        result.update(updated_list)

    return result
