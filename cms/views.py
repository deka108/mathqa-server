from django.shortcuts import render
from django.http import HttpResponseRedirect

from meas_models.models import *
from .forms import *
from meas_common.basic import *


# Topic
def topic_index(request, subject_id=-1):
    subject = ''
    if any(request.POST.getlist('subject')):
        subject_id = request.POST.__getitem__('subject')
        subject = Subject.objects.get(pk=subject_id)

    topics = Topic.objects.all if subject_id == - \
        1 else Subject.objects.get(pk=subject_id).topic_set.all()

    return render(request, 'cms/topic/index.html', __user_info(request, {
        "topics": topics,
        'form': SelectSubjectForm(initial={'subject': subject}),
    }))


def create_topic(request):
    return render(request, 'cms/topic/create.html', {'form': EditTopicForm()})


def edit_topic(request, topic_id):
    topic = Topic.objects.get(pk=topic_id)

    return render(request, 'cms/topic/edit.html', {'form': EditTopicForm(
        initial={'id': topic_id, 'name': topic.name,
                 'description': topic.description,
                 'subject': topic.subject
                 }
    )})


def api_create_topic(request):
    topic = Topic(name=request.POST.__getitem__('name'),
                  description=request.POST.__getitem__('description'),
                  subject=Subject.objects.get(
                      pk=request.POST.__getitem__('subject'))
                  )
    topic.save()

    return HttpResponseRedirect('../topic/', __user_info(request, {
        "topics": Topic.objects.all
    }))


def api_update_topic(request):
    topic = Topic.objects.get(pk=request.POST.__getitem__('id'))
    topic.name = request.POST.__getitem__('name')
    topic.description = request.POST.__getitem__('description')
    topic.subject = Subject.objects.get(pk=request.POST.__getitem__('subject'))

    topic.save()

    return HttpResponseRedirect('../topic/', __user_info(request, {
        "topics": Topic.objects.all
    }))


def delete_topic(request, topic_id):
    topic = Topic.objects.get(pk=topic_id)
    topic.delete()

    return HttpResponseRedirect('/cms/topic', __user_info(request, {
        "topics": Topic.objects.all(),
        'form': SelectSubjectForm(),
    }))


# Concept
def concept_index(request, topic_id=0):
    topics = ''
    subject = ''
    if topic_id != 0:
        concepts = Concept.objects.filter(topic=topic_id)
        subject = Topic.objects.get(pk=topic_id).subject
        topics = subject.topic_set.all()
    else:
        concepts = Concept.objects.all
        topics = Topic.objects.all

    return render(request, 'cms/concept/index.html', __user_info(request, {
        "topics": topics,
        "concepts": concepts,
        'form': SelectSubjectForm(initial={'subject': subject}),
    }))


def concept_subject(request):
    subject = ''

    if any(request.POST.getlist('subject')):
        subject_id = request.POST.__getitem__('subject')
        subject = Subject.objects.get(pk=subject_id)

    topics = Topic.objects.filter(
        subject=subject_id) if subject_id != 0 else Topic.objects.all

    return render(request, 'cms/concept/index.html', __user_info(request, {
        "topics": topics,
        'form': SelectSubjectForm(initial={'subject': subject}),
    }))


def create_concept(request):
    return render(request, 'cms/concept/create.html',
                  {'form': EditConceptForm()})


def edit_concept(request, concept_id):
    concept = Concept.objects.get(pk=concept_id)

    return render(request, 'cms/concept/edit.html', {'form': EditConceptForm(
        initial={'id': concept_id, 'name': concept.name,
                 'description': concept.description,
                 'topic': concept.topic
                 }
    )})


def api_create_concept(request):
    concept = Concept(name=request.POST.__getitem__('name'),
                      description=request.POST.__getitem__('description'),
                      topic=Topic.objects.get(
                      pk=request.POST.__getitem__('topic'))
                      )
    concept.save()

    return HttpResponseRedirect('../concept/', __user_info(request, {
        "topics": Topic.objects.all,
        "concepts": Concept.objects.all,
    }))


def api_update_concept(request):
    topic_id = request.POST.__getitem__('topic')

    concept = Concept.objects.get(pk=request.POST.__getitem__('id'))
    concept.name = request.POST.__getitem__('name')
    concept.description = request.POST.__getitem__('description')
    concept.topic = Topic.objects.get(pk=topic_id)

    concept.save()

    return HttpResponseRedirect('../concept/' + topic_id + '/',
                                __user_info(request, {
                                    "topics": Topic.objects.all
                                }))


def delete_concept(request, concept_id):
    concept = Concept.objects.get(pk=concept_id)
    concept.delete()

    return HttpResponseRedirect('/cms/concept', __user_info(request, {
        "topics": Topic.objects.all(),
        "concepts": Concept.objects.all(),
        'form': SelectSubjectForm(),
    }))


def question_index(request):
    return render(request, 'cms/question/index.html')


def create_question(request):
    return render(request, 'cms/question/create.html',
                  {'form': EditQuestionForm()})


def paper_index(request):
    return render(request, 'cms/paper/index.html', __user_info(request, {
        "papers": Paper.objects.all(),
    }))


def create_paper(request):
    return render(request, 'cms/paper/create.html',
                  {'form': EditPaperForm()})


def api_create_paper(request):
    paper = Paper(year=request.POST.__getitem__('year'),
                  month=request.POST.__getitem__('month'),
                  number=request.POST.__getitem__('number'))

    paper.save()

    return HttpResponseRedirect('../paper/', __user_info(request, {
        "papers": Paper.objects.all()
    }))


def edit_paper(request, paper_id):
    paper = Paper.objects.get(pk=paper_id)

    return render(request, 'cms/paper/edit.html', {'form': EditPaperForm(
        initial={'id': paper_id, 'year': paper.year,
                 'month': paper.get_month_display,
                 'number': paper.number
                 }
    )})


def api_update_paper(request):
    paper = Paper.objects.get(pk=request.POST.__getitem__('id'))
    paper.year = request.POST.__getitem__('year')
    paper.month = request.POST.__getitem__('month')
    paper.number = request.POST.__getitem__('number')

    paper.save()

    return HttpResponseRedirect('../paper/', __user_info(request, {
        "papers": Paper.objects.all()
    }))


def delete_paper(request, paper_id):
    paper = Paper.objects.get(pk=paper_id)
    paper.delete()

    return HttpResponseRedirect('/cms/paper', __user_info(request, {
        "papers": Paper.objects.all()
    }))

# Move up, down order


def move_up(request, topic_id):
    topic = Topic.objects.get(pk=topic_id)
    subject = topic.subject
    print subject

    if topic.order > 0:
        topic_swap = Topic.objects.get(order=int(topic.order) - 1)
        topic.order, topic_swap.order = swap_tmp(topic.order, topic_swap.order)

        topic.save()
        topic_swap.save()

    return HttpResponseRedirect('/cms/topic', __user_info(request, {
        "topics": subject.topic_set.all(),
        'form': SelectSubjectForm(initial={'subject': subject}),
    }))


# TODO: clean code later
# PhucLS
def move_down(request, topic_id):
    topic = Topic.objects.get(pk=topic_id)
    subject = topic.subject
    print subject

    if topic.order < Topic.objects.all().count() - 1:
        topic_swap = Topic.objects.get(order=int(topic.order) + 1)
        topic.order, topic_swap.order = swap_tmp(topic.order, topic_swap.order)

        topic.save()
        topic_swap.save()

    return HttpResponseRedirect('/cms/topic', __user_info(request, {
        "topics": subject.topic_set.all(),
        'form': SelectSubjectForm(initial={'subject': subject}),
    }))


def __user_info(request, updated_list=""):
    result = {
        'is_authenticated': request.user.is_authenticated,
        'current_user': request.user
    }

    if any(updated_list):
        result.update(updated_list)

    return result
