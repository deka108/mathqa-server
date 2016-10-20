from django.http import HttpResponse
from django.template import loader


# Dashboard
def dashboard_index(request):
    template = loader.get_template('webapp/dashboard/index.html')
    return HttpResponse(template.render(request))
# ------------------------------------------------------------------------------


# Adaptive Test
def adaptive_index(request):
    template = loader.get_template('webapp/adaptive_test/index.html')
    return HttpResponse(template.render(request))
# ------------------------------------------------------------------------------
