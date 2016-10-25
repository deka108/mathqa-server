from django.shortcuts import render


def dashboard_index(request):
    return render(request, 'webapp/dashboard/index.html', __user_info(request))


def adaptive_index(request):
    return render(request, 'webapp/adaptive_test/index.html',
                  __user_info(request))


def contest_index(request):
    return render(request, 'webapp/contest/index.html', __user_info(request))


def __user_info(request):
    return {
        'is_authenticated': request.user.is_authenticated,
        'current_user': request.user
    }
