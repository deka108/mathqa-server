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

    return render(request, 'cms/topic/create.html', __user_info(request, {
        'form': EditTopicForm()
    }))


def edit_topic(request, topic_id):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    topic = Topic.objects.get(pk=topic_id)

    return render(request, 'cms/topic/edit.html', __user_info(request, {
        'form': EditTopicForm(
            initial={'id': topic_id, 'name': topic.name,
                     'description': topic.description,
                     'subject': topic.subject
                     })}
    ))


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

    return render(request, 'cms/concept/create.html', __user_info(request, {
                  'form': EditConceptForm(), 'formset': formset
                  }))


def edit_concept(request, concept_id):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    concept = Concept.objects.get(pk=concept_id)

    KeyPointFormSet = formset_factory(KeyPointForm)
    res = []
    for k in concept.keypoint_set.all():
        res.append(k.__dict__)

    return render(request, 'cms/concept/edit.html', __user_info(request, {
        'form': EditConceptForm(
            initial={'id': concept_id, 'name': concept.name,
                     'description': concept.description,
                     'topic': concept.topic,
                     }),
        'formset': KeyPointFormSet(initial=res)
    }))


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

    # AnswerPart, Answer Sub Part
    EditAnswerPartFormSet = formset_factory(EditAnswerPartForm, extra=1)
    formset = EditAnswerPartFormSet(request.POST)

    if formset.is_valid():
        for f in formset:
            cd = f.cleaned_data
            if any(cd):
                if any(cd.get('part_name')):
                    answer_part = AnswerPart(part_name=cd.get('part_name'),
                                             part_content=cd.get(
                                                 'part_content'),
                                             part_respone_type=cd.get(
                                                 'part_respone_type'),
                                             question=question)
                    if (any(cd.get('subpart_name_1')) and
                            any(cd.get('subpart_content_1')) and
                            any(cd.get('respone_type_1'))):
                        answer_part.subpart_name_1 = cd.get('subpart_name_1')
                        answer_part.subpart_content_1 = cd.get(
                            'subpart_content_1')
                        answer_part.respone_type_1 = cd.get(
                            'respone_type_1')

                    if (any(cd.get('subpart_name_2')) and
                            any(cd.get('subpart_content_2')) and
                            any(cd.get('respone_type_2'))):
                        answer_part.subpart_name_2 = cd.get('subpart_name_2')
                        answer_part.subpart_content_2 = cd.get(
                            'subpart_content_2')
                        answer_part.respone_type_2 = cd.get(
                            'respone_type_2')

                    if (any(cd.get('subpart_name_3')) and
                            any(cd.get('subpart_content_3')) and
                            any(cd.get('respone_type_3'))):
                        answer_part.subpart_name_3 = cd.get('subpart_name_3')
                        answer_part.subpart_content_3 = cd.get(
                            'subpart_content_3')
                        answer_part.respone_type_3 = cd.get(
                            'respone_type_3')

                    if (any(cd.get('subpart_name_4')) and
                            any(cd.get('subpart_content_4')) and
                            any(cd.get('respone_type_4'))):
                        answer_part.subpart_name_4 = cd.get('subpart_name_4')
                        answer_part.subpart_content_4 = cd.get(
                            'subpart_content_4')
                        answer_part.respone_type_4 = cd.get(
                            'respone_type_4')

                    answer_part.save()

    return HttpResponseRedirect('../question/', __user_info(request, {
    }))


def create_question(request):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    EditAnswerPartFormSet = formset_factory(EditAnswerPartForm, extra=1)
    formset = EditAnswerPartFormSet()

    return render(request, 'cms/question/create.html',
                  {'form': EditQuestionForm(), 'formset': formset})


def edit_question(request, question_id):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    question = Question.objects.get(pk=question_id)

    EditAnswerPartFormSet = formset_factory(EditAnswerPartForm)

    res = []
    for k in question.answerpart_set.all():
        res.append(k.__dict__)

    return render(request, 'cms/question/edit.html', {'form': EditQuestionForm(
        initial={'id': question_id,
                 'question_type': question.question_type,
                 'source': question.source,
                 'used_for': question.used_for,
                 'mark': question.mark,
                 'difficulty_level': question.difficulty_level,
                 'respone_type': question.respone_type,
                 'content': question.content,
                 'solution': question.solution,
                 'concept': question.concept,
                 'paper': question.paper
                 }),
        'formset': EditAnswerPartFormSet(initial=res)
    })


def api_update_question(request):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    question = Question.objects.get(pk=request.POST.__getitem__('id'))
    question.question_type = request.POST.__getitem__('question_type')
    question.source = request.POST.__getitem__('source')
    question.used_for = request.POST.__getitem__('used_for')
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

    EditAnswerPartFormSet = formset_factory(EditAnswerPartForm)
    formset = EditAnswerPartFormSet(request.POST)

    if formset.is_valid():
        existing_answer_parts = question.answerpart_set.all()
        for answer_part in existing_answer_parts:
            counter = 0

            for f in formset:
                cd = f.cleaned_data

                if answer_part.part_name == cd.get('part_name'):
                    counter = counter + 1

            if counter == 0:
                answer_part.delete()

        for f in formset:
            cd = f.cleaned_data
            if any(cd):
                if (any(cd.get('part_name')) and
                        any(cd.get('part_content')) and
                        any(cd.get('part_respone_type'))):
                    answer_part = AnswerPart.objects.filter(
                        part_name=cd.get('part_name'),
                        question=question).first()
                    if answer_part is None:
                        answer_part = AnswerPart(question=question)

                    answer_part.part_name = cd.get('part_name')
                    answer_part.part_content = cd.get('part_content')
                    answer_part.part_respone_type = cd.get('part_respone_type')

                    if (any(cd.get('subpart_name_1')) and
                            any(cd.get('subpart_content_1')) and
                            any(cd.get('respone_type_1'))):
                        answer_part.subpart_name_1 = cd.get('subpart_name_1')
                        answer_part.subpart_content_1 = cd.get(
                            'subpart_content_1')
                        answer_part.respone_type_1 = cd.get(
                            'respone_type_1')

                    if (any(cd.get('subpart_name_2')) and
                            any(cd.get('subpart_content_2')) and
                            any(cd.get('respone_type_2'))):
                        answer_part.subpart_name_2 = cd.get('subpart_name_2')
                        answer_part.subpart_content_2 = cd.get(
                            'subpart_content_2')
                        answer_part.respone_type_2 = cd.get(
                            'respone_type_2')

                    if (any(cd.get('subpart_name_3')) and
                            any(cd.get('subpart_content_3')) and
                            any(cd.get('respone_type_3'))):
                        answer_part.subpart_name_3 = cd.get('subpart_name_3')
                        answer_part.subpart_content_3 = cd.get(
                            'subpart_content_3')
                        answer_part.respone_type_3 = cd.get(
                            'respone_type_3')

                    if (any(cd.get('subpart_name_4')) and
                            any(cd.get('subpart_content_4')) and
                            any(cd.get('respone_type_4'))):
                        answer_part.subpart_name_4 = cd.get('subpart_name_4')
                        answer_part.subpart_content_4 = cd.get(
                            'subpart_content_4')
                        answer_part.respone_type_4 = cd.get(
                            'respone_type_4')

                    answer_part.save()

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

    return render(request, 'cms/paper/create.html', __user_info(request, {
                  'form': EditPaperForm()}))


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

    return render(request, 'cms/user/create.html', __user_info(request, {
                  'form': EditUserForm()}))


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
