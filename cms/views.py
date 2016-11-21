"""
# Name:           cms/views.py
# Description:
# Created by:     Phuc Le-Sanh
# Date Created:   Nov 16 2016
# Last Modified:  Nov 16 2016
# Modified by:    Phuc Le-Sanh
"""
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.forms import formset_factory

from meas_models.models import *
from .forms import *
from meas_common.basic import *


# Topic
def topic_index(request, subject_id=-1):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

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
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    return render(request, 'cms/topic/create.html', {'form': EditTopicForm()})


def edit_topic(request, topic_id):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    topic = Topic.objects.get(pk=topic_id)

    return render(request, 'cms/topic/edit.html', {'form': EditTopicForm(
        initial={'id': topic_id, 'name': topic.name,
                 'description': topic.description,
                 'subject': topic.subject
                 }
    )})


def api_create_topic(request):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

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
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    topic = Topic.objects.get(pk=request.POST.__getitem__('id'))
    topic.name = request.POST.__getitem__('name')
    topic.description = request.POST.__getitem__('description')
    topic.subject = Subject.objects.get(pk=request.POST.__getitem__('subject'))

    topic.save()

    return HttpResponseRedirect('../topic/', __user_info(request, {
        "topics": Topic.objects.all
    }))


def delete_topic(request, topic_id):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    topic = Topic.objects.get(pk=topic_id)
    topic.delete()

    return HttpResponseRedirect('/cms/topic', __user_info(request, {
        "topics": Topic.objects.all(),
        'form': SelectSubjectForm(),
    }))


# Concept
def concept_index(request, topic_id=0):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

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
    if not request.user.is_superuser:
        return redirect('/cms/login/')

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
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    KeyPointFormSet = formset_factory(KeyPointForm, extra=1)
    formset = KeyPointFormSet()

    return render(request, 'cms/concept/create.html',
                  {'form': EditConceptForm(), 'formset': formset})


def edit_concept(request, concept_id):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    concept = Concept.objects.get(pk=concept_id)

    KeyPointFormSet = formset_factory(KeyPointForm)
    res = []
    for k in concept.keypoint_set.all():
        res.append(k.__dict__)

    return render(request, 'cms/concept/edit.html', {
        'form': EditConceptForm(
            initial={'id': concept_id, 'name': concept.name,
                     'description': concept.description,
                     'topic': concept.topic,
                     }),
        'formset': KeyPointFormSet(initial=res)
    })


def api_create_concept(request):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    concept = Concept(name=request.POST.__getitem__('name'),
                      description=request.POST.__getitem__('description'),
                      topic=Topic.objects.get(
        pk=request.POST.__getitem__('topic'))
    )
    concept.save()

    # Complement formset
    KeyPointFormSet = formset_factory(KeyPointForm)
    formset = KeyPointFormSet(request.POST)
    if formset.is_valid():
        for f in formset:
            cd = f.cleaned_data
            if any(cd):
                keypoint = KeyPoint(name=cd.get('name'),
                                    content=cd.get('content'),
                                    concept=concept)
                keypoint.save()

    return HttpResponseRedirect('../concept/', __user_info(request, {
        "topics": Topic.objects.all,
        "concepts": Concept.objects.all,
    }))


def api_update_concept(request):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    topic_id = request.POST.__getitem__('topic')

    concept = Concept.objects.get(pk=request.POST.__getitem__('id'))
    concept.name = request.POST.__getitem__('name')
    concept.description = request.POST.__getitem__('description')
    concept.topic = Topic.objects.get(pk=topic_id)

    concept.save()

    # Complement formset
    KeyPointFormSet = formset_factory(KeyPointForm)
    formset = KeyPointFormSet(request.POST)

    if formset.is_valid():
        # Temporarily fix for removing key points - PhucLS
        existing_keypoints = concept.keypoint_set.all()
        for keypoint in existing_keypoints:
            counter = 0

            for f in formset:
                cd = f.cleaned_data

                if keypoint.name == cd.get('name'):
                    counter = counter + 1

            if counter == 0:
                keypoint.delete()

        for f in formset:
            cd = f.cleaned_data

            update_name = cd.get('name')
            update_content = cd.get('content')

            keypoint = KeyPoint.objects.filter(name=update_name).first()
            if keypoint:
                keypoint.content = update_content
                keypoint.save()
            elif (update_name is not None and update_content is not None):
                keypoint = KeyPoint(name=update_name,
                                    content=update_content,
                                    concept=concept)
                keypoint.save()

    return HttpResponseRedirect('../concept/' + topic_id + '/',
                                __user_info(request, {
                                    "topics": Topic.objects.all
                                }))


def delete_concept(request, concept_id):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    concept = Concept.objects.get(pk=concept_id)
    concept.delete()

    return HttpResponseRedirect('/cms/concept', __user_info(request, {
        "topics": Topic.objects.all(),
        "concepts": Concept.objects.all(),
        'form': SelectSubjectForm(),
    }))


def question_index(request):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    return render(request, 'cms/question/index.html', __user_info(request, {
        "topics": Topic.objects.all(),
        "papers": Paper.objects.all(),
    }))


def api_create_question(request):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    question = Question(
        question_type=request.POST.__getitem__('question_type'),
        source=request.POST.__getitem__('source'),
        used_for=request.POST.__getitem__('used_for'),
        number_of_part=request.POST.__getitem__(
            'number_of_part'),
        mark=request.POST.__getitem__('mark'),
        difficulty_level=request.POST.__getitem__(
            'difficulty_level'),
        content=request.POST.__getitem__('content'),
        solution=request.POST.__getitem__('solution'),
        concept=Concept.objects.get(pk=request.POST.__getitem__('concept')),
    )

    if any(request.POST.getlist('keypoint')):
        question.keypoint = KeyPoint.objects.get(
            pk=request.POST.__getitem__('keypoint'))

    if any(request.POST.getlist('paper')):
        question.paper = Paper.objects.get(
            pk=request.POST.__getitem__('paper'))

    question.save()

    # Add Parts
    if (any(request.POST.getlist('mark_1')) and
            (int(question.number_of_part) >= 1)):
        part1 = Part(
            mark=request.POST.__getitem__('mark_1'),
            difficulty_level=request.POST.__getitem__(
                'difficulty_level_1'),
            respone_type=request.POST.__getitem__('respone_type_1'),
            content=request.POST.__getitem__('content_1'),
            solution=request.POST.__getitem__('solution_1'),
            question=question,
        )
        part1.save()

    if (any(request.POST.getlist('mark_2')) and
            (int(question.number_of_part) >= 2)):
        part2 = Part(
            mark=request.POST.__getitem__('mark_2'),
            difficulty_level=request.POST.__getitem__('difficulty_level_2'),
            respone_type=request.POST.__getitem__('respone_type_2'),
            content=request.POST.__getitem__('content_2'),
            solution=request.POST.__getitem__('solution_2'),
            question=question,
        )
        part2.save()

    if (any(request.POST.getlist('mark_3')) and
            (int(question.number_of_part) >= 3)):
        part3 = Part(
            mark=request.POST.__getitem__('mark_3'),
            difficulty_level=request.POST.__getitem__('difficulty_level_3'),
            respone_type=request.POST.__getitem__('respone_type_3'),
            content=request.POST.__getitem__('content_3'),
            solution=request.POST.__getitem__('solution_3'),
            question=question,
        )
        part3.save()

    if (any(request.POST.getlist('mark_4')) and
            (int(question.number_of_part) == 4)):
        part4 = Part(
            mark=request.POST.__getitem__('mark_4'),
            difficulty_level=request.POST.__getitem__('difficulty_level_4'),
            respone_type=request.POST.__getitem__('respone_type_4'),
            content=request.POST.__getitem__('content_4'),
            solution=request.POST.__getitem__('solution_4'),
            question=question,
        )
        part4.save()

    return HttpResponseRedirect('../question/', __user_info(request, {
    }))


def create_question(request):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    return render(request, 'cms/question/create.html',
                  {'form': EditQuestionForm()})


def edit_question(request, question_id):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    question = Question.objects.get(pk=question_id)
    parts = question.part_set.all()

    return render(request, 'cms/question/edit.html', {'form': EditQuestionForm(
        initial=__parts({'id': question_id,
                         'question_type': question.question_type,
                         'source': question.source,
                         'used_for': question.used_for,
                         'number_of_part': question.number_of_part,
                         'mark': question.mark,
                         'difficulty_level': question.difficulty_level,
                         'respone_type': question.respone_type,
                         'content': question.content,
                         'solution': question.solution,
                         'concept': question.concept,
                         'paper': question.paper
                         }, parts)
    )})


def api_update_question(request):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    question = Question.objects.get(pk=request.POST.__getitem__('id'))
    question.question_type = request.POST.__getitem__('question_type')
    question.source = request.POST.__getitem__('source')
    question.used_for = request.POST.__getitem__('used_for')
    question.number_of_part = request.POST.__getitem__('number_of_part')
    question.mark = request.POST.__getitem__('mark')
    question.difficulty_level = request.POST.__getitem__('difficulty_level')
    question.respone_type = request.POST.__getitem__('respone_type')
    question.content = request.POST.__getitem__('content')
    question.solution = request.POST.__getitem__('solution')

    if any(request.POST.getlist('keypoint')):
        question.keypoint = KeyPoint.objects.get(
            pk=request.POST.__getitem__('keypoint'))

    question.concept = Concept.objects.get(
        pk=request.POST.__getitem__('concept'))

    if any(request.POST.getlist('paper')):
        question.paper = Paper.objects.get(
            pk=request.POST.__getitem__('paper'))

    question.save()

    # Update Parts
    if (any(request.POST.getlist('mark_1')) and
            (int(question.number_of_part) >= 1)):
        checking = Part.objects.get(pk=request.POST.__getitem__('id_1'))

        if checking:
            part_1 = Part.objects.get(pk=request.POST.__getitem__('id_1'))
            part_1.mark = request.POST.__getitem__('mark_1')
            part_1.difficulty_level = request.POST.__getitem__(
                'difficulty_level_1')
            part_1.respone_type = request.POST.__getitem__('respone_type_1')
            part_1.content = request.POST.__getitem__('content_1')
            part_1.solution = request.POST.__getitem__('solution_1')
            part_1.question = question
            part_1.save()
        else:
            part_1 = Part(
                mark=request.POST.__getitem__('mark_1'),
                difficulty_level=request.POST.__getitem__(
                    'difficulty_level_1'),
                respone_type=request.POST.__getitem__('respone_type_1'),
                content=request.POST.__getitem__('content_1'),
                solution=request.POST.__getitem__('solution_1'),
                question=question)
            part_1.save()

    if (any(request.POST.getlist('mark_2')) and
            (int(question.number_of_part) >= 2)):
        checking = Part.objects.get(pk=request.POST.__getitem__('id_2'))

        if checking:
            part_2 = Part.objects.get(pk=request.POST.__getitem__('id_2'))
            part_2.mark = request.POST.__getitem__('mark_2')
            part_2.difficulty_level = request.POST.__getitem__(
                'difficulty_level_2')
            part_2.respone_type = request.POST.__getitem__('respone_type_2')
            part_2.content = request.POST.__getitem__('content_2')
            part_2.solution = request.POST.__getitem__('solution_2')
            part_2.question = question
            part_2.save()
        else:
            part_2 = Part(
                mark=request.POST.__getitem__('mark_2'),
                difficulty_level=request.POST.__getitem__(
                    'difficulty_level_2'),
                respone_type=request.POST.__getitem__('respone_type_2'),
                content=request.POST.__getitem__('content_2'),
                solution=request.POST.__getitem__('solution_2'),
                question=question)
            part_2.save()

    if (any(request.POST.getlist('mark_3')) and
            (int(question.number_of_part) >= 3)):
        checking = Part.objects.get(pk=request.POST.__getitem__('id_3'))

        if checking:
            part_3 = Part.objects.get(pk=request.POST.__getitem__('id_3'))
            part_3.mark = request.POST.__getitem__('mark_3')
            part_3.difficulty_level = request.POST.__getitem__(
                'difficulty_level_3')
            part_3.respone_type = request.POST.__getitem__('respone_type_3')
            part_3.content = request.POST.__getitem__('content_3')
            part_3.solution = request.POST.__getitem__('solution_3')
            part_3.question = question
            part_3.save()
        else:
            part_3 = Part(
                mark=request.POST.__getitem__('mark_3'),
                difficulty_level=request.POST.__getitem__(
                    'difficulty_level_3'),
                respone_type=request.POST.__getitem__('respone_type_3'),
                content=request.POST.__getitem__('content_3'),
                solution=request.POST.__getitem__('solution_3'),
                question=question)
            part_3.save()

    if (any(request.POST.getlist('mark_4')) and
            (int(question.number_of_part) == 4)):
        checking = Part.objects.get(pk=request.POST.__getitem__('id_4'))

        if checking:
            part_4 = Part.objects.get(pk=request.POST.__getitem__('id_4'))
            part_4.mark = request.POST.__getitem__('mark_4')
            part_4.difficulty_level = request.POST.__getitem__(
                'difficulty_level_4')
            part_4.respone_type = request.POST.__getitem__('respone_type_4')
            part_4.content = request.POST.__getitem__('content_4')
            part_4.solution = request.POST.__getitem__('solution_4')
            part_4.question = question
            part_4.save()
        else:
            part_4 = Part(
                mark=request.POST.__getitem__('mark_4'),
                difficulty_level=request.POST.__getitem__(
                    'difficulty_level_4'),
                respone_type=request.POST.__getitem__('respone_type_4'),
                content=request.POST.__getitem__('content_4'),
                solution=request.POST.__getitem__('solution_4'),
                question=question)
            part_4.save()

    return HttpResponseRedirect('../question/', __user_info(request, {
    }))


def delete_question(request, question_id):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    question = Question.objects.get(pk=question_id)
    question.delete()

    return HttpResponseRedirect('/cms/question', __user_info(request, {
        "topics": Topic.objects.all(),
        "papers": Paper.objects.all(),
    }))


def question_topic_detail(request, topic_id):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    topic = Topic.objects.get(pk=topic_id)
    concept = topic.concept_set.all()

    return render(request, 'cms/question/index.html', __user_info(request, {
        "topic_name": topic.name,
        "topics": Topic.objects.all(),
        "papers": Paper.objects.all(),
        "questions": Question.objects.filter(concept__in=concept,
                                             question_type="PR"),
    }))


def question_paper_detail(request, paper_id):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    paper = Paper.objects.get(pk=paper_id)

    return render(request, 'cms/question/index.html', __user_info(request, {
        "topics": Topic.objects.all(),
        "papers": Paper.objects.all(),
        "questions": Question.objects.filter(paper=paper,
                                             question_type="EX"),
    }))


def paper_index(request):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    return render(request, 'cms/paper/index.html', __user_info(request, {
        "papers": Paper.objects.all(),
    }))


def create_paper(request):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    return render(request, 'cms/paper/create.html',
                  {'form': EditPaperForm()})


def api_create_paper(request):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    paper = Paper(year=request.POST.__getitem__('year'),
                  month=request.POST.__getitem__('month'),
                  number=request.POST.__getitem__('number'))

    paper.save()

    return HttpResponseRedirect('../paper/', __user_info(request, {
        "papers": Paper.objects.all()
    }))


def edit_paper(request, paper_id):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    paper = Paper.objects.get(pk=paper_id)

    return render(request, 'cms/paper/edit.html', {'form': EditPaperForm(
        initial={'id': paper_id, 'year': paper.year,
                 'month': paper.get_month_display,
                 'number': paper.number
                 }
    )})


def api_update_paper(request):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    paper = Paper.objects.get(pk=request.POST.__getitem__('id'))
    paper.year = request.POST.__getitem__('year')
    paper.month = request.POST.__getitem__('month')
    paper.number = request.POST.__getitem__('number')

    paper.save()

    return HttpResponseRedirect('../paper/', __user_info(request, {
        "papers": Paper.objects.all()
    }))


def delete_paper(request, paper_id):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    paper = Paper.objects.get(pk=paper_id)
    paper.delete()

    return HttpResponseRedirect('/cms/paper', __user_info(request, {
        "papers": Paper.objects.all()
    }))


def user_index(request):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    return render(request, 'cms/user/index.html', __user_info(request, {
        "users": User.objects.all(),
    }))


def create_user(request):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    return render(request, 'cms/user/create.html',
                  {'form': EditUserForm()})


def api_create_user(request):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    User.objects.create_user(username=request.POST.__getitem__('username'),
                             password=request.POST.__getitem__('password'),
                             email=request.POST.__getitem__('email'),
                             first_name=request.POST.__getitem__('first_name'),
                             last_name=request.POST.__getitem__('last_name'),
                             is_staff=request.POST.__getitem__('is_staff'),
                             is_active=request.POST.__getitem__('is_active')
                             )

    return HttpResponseRedirect('../user/', __user_info(request, {
        "users": User.objects.all()
    }))


def edit_user(request, user_id):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    user = User.objects.get(pk=user_id)

    return render(request, 'cms/user/edit.html', {'form': EditUserForm(
        initial={'id': user_id,
                 'username': user.username,
                 'password': user.password,
                 'email': user.email,
                 'first_name': user.first_name,
                 'last_name': user.last_name,
                 'is_staff': user.is_staff,
                 'is_active': user.is_active
                 }
    )})


def api_update_user(request):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    user = User.objects.get(pk=request.POST.__getitem__('id'))
    user.username = request.POST.__getitem__('username')
    user.password = request.POST.__getitem__('password')
    user.email = request.POST.__getitem__('email')
    user.first_name = request.POST.__getitem__('first_name')
    user.last_name = request.POST.__getitem__('last_name')
    user.is_staff = request.POST.__getitem__('is_staff')
    user.is_active = request.POST.__getitem__('is_active')

    user.save()

    return HttpResponseRedirect('../user/', __user_info(request, {
        "users": User.objects.all()
    }))


def delete_user(request, user_id):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    user = User.objects.get(pk=user_id)
    user.delete()

    return HttpResponseRedirect('/cms/user', __user_info(request, {
        "users": User.objects.all()
    }))
# Move up, down order


def move_up(request, topic_id):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    topic = Topic.objects.get(pk=topic_id)
    subject = topic.subject

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
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    topic = Topic.objects.get(pk=topic_id)
    subject = topic.subject

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


def __parts(clist, parts):
    i = 1
    for part in parts:
        hash_part = {
            'id_' + str(i): part.id,
            'mark_' + str(i): part.mark,
            'difficulty_level_' + str(i): part.difficulty_level,
            'respone_type_' + str(i): part.respone_type,
            'content_' + str(i): part.content,
            'solution_' + str(i): part.solution,
        }
        clist.update(hash_part)
        i = i + 1
    return clist
