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

import re


# Topic
def topic_index(request, subject_id=-1):
    if not request.user.is_superuser:
        return redirect('/login/')

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
        return redirect('/login/')

    return render(request, 'cms/topic/create.html', __user_info(request, {
        'form': EditTopicForm()
    }))


def edit_topic(request, topic_id):
    if not request.user.is_superuser:
        return redirect('/login/')

    topic = Topic.objects.get(pk=topic_id)

    return render(request, 'cms/topic/edit.html', __user_info(request, {
        'form': EditTopicForm(
            initial={'id': topic_id, 'name': topic.name,
                     'description': topic.description,
                     'subject': topic.subject,
                     'order': topic.order
                     })}
    ))


def api_create_topic(request):
    if not request.user.is_superuser:
        return redirect('/login/')

    topic = Topic(name=request.POST.__getitem__('name'),
                  description=request.POST.__getitem__('description'),
                  order=request.POST.__getitem__('order'),
                  subject=Subject.objects.get(
        pk=request.POST.__getitem__('subject'))
    )
    topic.save()

    return HttpResponseRedirect('../topic/', __user_info(request, {
        "topics": Topic.objects.all
    }))


def api_update_topic(request):
    if not request.user.is_superuser:
        return redirect('/login/')

    topic = Topic.objects.get(pk=request.POST.__getitem__('id'))
    topic.name = request.POST.__getitem__('name')
    topic.description = request.POST.__getitem__('description')
    topic.order = request.POST.__getitem__('order')
    topic.subject = Subject.objects.get(pk=request.POST.__getitem__('subject'))

    topic.save()

    return HttpResponseRedirect('../topic/', __user_info(request, {
        "topics": Topic.objects.all
    }))


def delete_topic(request, topic_id):
    if not request.user.is_superuser:
        return redirect('/login/')

    topic = Topic.objects.get(pk=topic_id)
    topic.delete()

    return HttpResponseRedirect('/cms/topic/', __user_info(request, {
        "topics": Topic.objects.all(),
        'form': SelectSubjectForm(),
    }))


# Concept
def concept_index(request, topic_id=0):
    if not request.user.is_superuser:
        return redirect('/login/')

    topics = ''
    subject = ''
    if topic_id != 0:
        concepts = Concept.objects.filter(topic=topic_id)
        subject = Topic.objects.get(pk=topic_id).subject
        topics = Topic.objects.all
        # topics = subject.topic_set.all()
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
        return redirect('/login/')

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
        return redirect('/login/')

    KeyPointFormSet = formset_factory(KeyPointForm, extra=1)
    formset = KeyPointFormSet()

    return render(request, 'cms/concept/create.html', __user_info(request, {
                  'form': EditConceptForm(), 'formset': formset
                  }))


def edit_concept(request, concept_id):
    if not request.user.is_superuser:
        return redirect('/login/')

    concept = Concept.objects.get(pk=concept_id)

    extra_keypoint = 0
    if concept.keypoint_set.all().count() == 0:
        extra_keypoint = 1

    KeyPointFormSet = formset_factory(KeyPointForm, extra=extra_keypoint)

    res = []
    for k in concept.keypoint_set.all():
        res.append(k.__dict__)

    return render(request, 'cms/concept/edit.html', __user_info(request, {
        'form': EditConceptForm(
            initial={'id': concept_id, 'name': concept.name,
                     'description': concept.description,
                     'topic': concept.topic,
                     'order': concept.order,
                     }),
        'formset': KeyPointFormSet(initial=res)
    }))


def api_create_concept(request):
    if not request.user.is_superuser:
        return redirect('/login/')

    concept = Concept(name=request.POST.__getitem__('name'),
                      description=request.POST.__getitem__('description'),
                      order=request.POST.__getitem__('order'),
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
        return redirect('/login/')

    topic_id = request.POST.__getitem__('topic')

    concept = Concept.objects.get(pk=request.POST.__getitem__('id'))
    concept.name = request.POST.__getitem__('name')
    concept.description = request.POST.__getitem__('description')
    concept.order = request.POST.__getitem__('order')
    concept.topic = Topic.objects.get(pk=topic_id)

    concept.save()

    KeyPointFormSet = formset_factory(KeyPointForm)
    formset = KeyPointFormSet(request.POST)

    if formset.is_valid():
        existing_keypoints = concept.keypoint_set.all()
        for keypoint in existing_keypoints:
            keypoint.delete()
            print "delete"

        for f in formset:
            cd = f.cleaned_data

            keypoint = KeyPoint(name=cd.get('name'),
                                content=cd.get('content'),
                                concept=concept)
            keypoint.save()

    return HttpResponseRedirect('../concept/', __user_info(request, {
        "concepts": Concept.objects.all
    }))


def delete_concept(request, concept_id):
    if not request.user.is_superuser:
        return redirect('/login/')

    concept = Concept.objects.get(pk=concept_id)
    concept.delete()

    return HttpResponseRedirect('/cms/concept', __user_info(request, {
        "topics": Topic.objects.all(),
        "concepts": Concept.objects.all(),
        'form': SelectSubjectForm(),
    }))


def question_index(request):
    if not request.user.is_superuser:
        return redirect('/login/')

    return render(request, 'cms/question/index.html', __user_info(request, {
        "topics": Topic.objects.all(),
        "papers": Paper.objects.all(),
    }))


def question_paper(request):
    if not request.user.is_superuser:
        return redirect('/login/')

    return render(request, 'cms/question/paper.html', __user_info(request, {
        "papers": Paper.objects.all(),
        "questions": Question.objects.filter(question_type="PR")
    }))


def api_create_question(request):
    if not request.user.is_superuser:
        return redirect('/login/')

    question = ""

    if any(request.POST.__getitem__('answer')):
        question = Question(
            question_type=request.POST.__getitem__('question_type'),
            used_for=request.POST.__getitem__('used_for'),
            mark=request.POST.__getitem__('mark'),
            difficulty_level=request.POST.__getitem__(
                'difficulty_level'),
            content=request.POST.__getitem__('content'),
            solution=request.POST.__getitem__('solution'),
            answer=request.POST.__getitem__('answer'),
            concept=Concept.objects.get(pk=request.POST.__getitem__('concept'))
        )
    else:
        question = Question(
            question_type=request.POST.__getitem__('question_type'),
            used_for=request.POST.__getitem__('used_for'),
            mark=request.POST.__getitem__('mark'),
            difficulty_level=request.POST.__getitem__(
                'difficulty_level'),
            content=request.POST.__getitem__('content'),
            solution=request.POST.__getitem__('solution'),
            concept=Concept.objects.get(pk=request.POST.__getitem__('concept'))
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
                    if (any(cd.get('subpart_content_1')) and
                            any(cd.get('respone_type_1'))):
                        answer_part.subpart_name_1 = "i"
                        answer_part.subpart_content_1 = cd.get(
                            'subpart_content_1')
                        answer_part.respone_type_1 = cd.get(
                            'respone_type_1')

                    if (any(cd.get('subpart_content_2')) and
                            any(cd.get('respone_type_2'))):
                        answer_part.subpart_name_2 = "ii"
                        answer_part.subpart_content_2 = cd.get(
                            'subpart_content_2')
                        answer_part.respone_type_2 = cd.get(
                            'respone_type_2')

                    if (any(cd.get('subpart_content_3')) and
                            any(cd.get('respone_type_3'))):
                        answer_part.subpart_name_3 = "iii"
                        answer_part.subpart_content_3 = cd.get(
                            'subpart_content_3')
                        answer_part.respone_type_3 = cd.get(
                            'respone_type_3')

                    if (any(cd.get('subpart_content_4')) and
                            any(cd.get('respone_type_4'))):
                        answer_part.subpart_name_4 = "iv"
                        answer_part.subpart_content_4 = cd.get(
                            'subpart_content_4')
                        answer_part.respone_type_4 = cd.get(
                            'respone_type_4')

                    answer_part.save()

    # Description:  Add formulas
    # Author:       PhucLS
    # Date:         Jan 05, 2017
    for f_id in request.POST.getlist('formula'):
        question.formulas.add(Formula.objects.get(pk=f_id))

    return HttpResponseRedirect('../question/', __user_info(request, {
    }))


def create_question(request):
    if not request.user.is_superuser:
        return redirect('/login/')

    EditAnswerPartFormSet = formset_factory(EditAnswerPartForm, extra=1)
    formset = EditAnswerPartFormSet()

    return render(request, 'cms/question/create.html',
                  __user_info(request,
                              {'form': EditQuestionForm(),
                               'formset': formset}))


def edit_question(request, question_id):
    if not request.user.is_superuser:
        return redirect('/login/')

    question = Question.objects.get(pk=question_id)

    EditAnswerPartFormSet = formset_factory(EditAnswerPartForm)

    res = []
    for k in question.answerpart_set.all():
        res.append(k.__dict__)

    return render(request, 'cms/question/edit.html', {'form': EditQuestionForm(
        initial={'id': question_id,
                 'question_type': question.question_type,
                 'used_for': question.used_for,
                 'mark': question.mark,
                 'difficulty_level': question.difficulty_level,
                 'respone_type': question.respone_type,
                 'content': question.content,
                 'answer': question.answer,
                 'solution': question.solution,
                 'concept': question.concept,
                 'paper': question.paper
                 }),
        'formset': EditAnswerPartFormSet(initial=res)
    })


def api_update_question(request):
    if not request.user.is_superuser:
        return redirect('/login/')

    question = Question.objects.get(pk=request.POST.__getitem__('id'))
    question.question_type = request.POST.__getitem__('question_type')
    question.used_for = request.POST.__getitem__('used_for')
    question.mark = request.POST.__getitem__('mark')
    question.difficulty_level = request.POST.__getitem__('difficulty_level')
    question.respone_type = request.POST.__getitem__('respone_type')

    if any(request.POST.__getitem__('answer')):
        question.answer = request.POST.__getitem__('answer')
    else:
        question.answer = ""

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

                    if (any(cd.get('subpart_content_1')) and
                            any(cd.get('respone_type_1'))):
                        answer_part.subpart_name_1 = "i"
                        answer_part.subpart_content_1 = cd.get(
                            'subpart_content_1')
                        answer_part.respone_type_1 = cd.get(
                            'respone_type_1')

                    if (any(cd.get('subpart_content_2')) and
                            any(cd.get('respone_type_2'))):
                        answer_part.subpart_name_2 = "ii"
                        answer_part.subpart_content_2 = cd.get(
                            'subpart_content_2')
                        answer_part.respone_type_2 = cd.get(
                            'respone_type_2')

                    if (any(cd.get('subpart_content_3')) and
                            any(cd.get('respone_type_3'))):
                        answer_part.subpart_name_3 = "iii"
                        answer_part.subpart_content_3 = cd.get(
                            'subpart_content_3')
                        answer_part.respone_type_3 = cd.get(
                            'respone_type_3')

                    if (any(cd.get('subpart_content_4')) and
                            any(cd.get('respone_type_4'))):
                        answer_part.subpart_name_4 = "iv"
                        answer_part.subpart_content_4 = cd.get(
                            'subpart_content_4')
                        answer_part.respone_type_4 = cd.get(
                            'respone_type_4')

                    answer_part.save()

    # Description:  Add formulas
    # Author:       PhucLS
    # Date:         Jan 05, 2017
    for f_id in request.POST.getlist('formula'):
        question.formulas.add(Formula.objects.get(pk=f_id))
    return HttpResponseRedirect('../question/', __user_info(request, {
    }))


def delete_question(request, question_id):
    if not request.user.is_superuser:
        return redirect('/login/')

    question = Question.objects.get(pk=question_id)
    question.delete()

    return HttpResponseRedirect('/cms/question', __user_info(request, {
        "topics": Topic.objects.all(),
        "papers": Paper.objects.all(),
    }))


def question_topic_detail(request, topic_id):
    if not request.user.is_superuser:
        return redirect('/login/')

    topic = Topic.objects.get(pk=topic_id)
    concept = topic.concept_set.all()
    questions = Question.objects.filter(concept__in=concept, question_type="PR")
    for question in questions:
        question = format_answer_box(question)

    return render(request, 'cms/question/questions.html', __user_info(
        request, {"questions": questions}))


def question_paper_detail(request, paper_id):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    paper = Paper.objects.get(pk=paper_id)

    return render(request, 'cms/question/paper.html', __user_info(request, {
        "topics": Topic.objects.all(),
        "papers": Paper.objects.all(),
        "questions": Question.objects.filter(paper=paper,
                                             question_type="EX"),
    }))


def paper_index(request, subject_id=-1):
    if not request.user.is_superuser:
        return redirect('/login/')

    subject = ''
    if any(request.POST.getlist('subject')):
        subject_id = request.POST.__getitem__('subject')
        subject = Subject.objects.get(pk=subject_id)

    papers = Paper.objects.all if subject_id == - \
        1 else Subject.objects.get(pk=subject_id).paper_set.all()

    return render(request, 'cms/paper/index.html', __user_info(request, {
        "papers": papers,
        'form': SelectSubjectForm(initial={'subject': subject})
    }))


def create_paper(request):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    return render(request, 'cms/paper/create.html', __user_info(request, {
                  'form': EditPaperForm()}))


def api_create_paper(request):
    if not request.user.is_superuser:
        return redirect('/login/')

    paper = Paper(year=request.POST.__getitem__('year'),
                  month=request.POST.__getitem__('month'),
                  number=request.POST.__getitem__('number'),
                  subject=Subject.objects.get(
                      pk=request.POST.__getitem__('subject')))

    paper.save()

    return HttpResponseRedirect('../paper/', __user_info(request, {
        "papers": Paper.objects.all()
    }))


def edit_paper(request, paper_id):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    paper = Paper.objects.get(pk=paper_id)

    return render(request, 'cms/paper/edit.html', __user_info(request, {
        'form': EditPaperForm(initial={'id': paper_id, 'year': paper.year,
                                       'month': paper.get_month_display,
                                       'number': paper.number,
                                       'subject': paper.subject
                                       })}))


def api_update_paper(request):
    if not request.user.is_superuser:
        return redirect('/login/')

    paper = Paper.objects.get(pk=request.POST.__getitem__('id'))
    paper.year = request.POST.__getitem__('year')
    paper.month = request.POST.__getitem__('month')
    paper.number = request.POST.__getitem__('number')
    paper.subject = Subject.objects.get(
        pk=request.POST.__getitem__('subject'))
    paper.save()

    return HttpResponseRedirect('../paper/', __user_info(request, {
        "papers": Paper.objects.all()
    }))


def delete_paper(request, paper_id):
    if not request.user.is_superuser:
        return redirect('/login/')

    paper = Paper.objects.get(pk=paper_id)
    paper.delete()

    return HttpResponseRedirect('/cms/paper', __user_info(request, {
        "papers": Paper.objects.all()
    }))


def user_index(request):
    if not request.user.is_superuser:
        return redirect('/login/')

    return render(request, 'cms/user/index.html', __user_info(request, {
        "users": User.objects.all(),
    }))


def create_user(request):
    if not request.user.is_superuser:
        return redirect('/login/')

    return render(request, 'cms/user/create.html', __user_info(request, {
                  'form': EditUserForm()}))


def api_create_user(request):
    if not request.user.is_superuser:
        return redirect('/login/')

    User.objects.create_user(username=request.POST.__getitem__('username'),
                             password=request.POST.__getitem__('password'),
                             email=request.POST.__getitem__('email'),
                             first_name=request.POST.__getitem__('first_name'),
                             last_name=request.POST.__getitem__('last_name'),
                             is_staff=False,
                             is_active=request.POST.__getitem__('is_active')
                             )

    return HttpResponseRedirect('../user/', __user_info(request, {
        "users": User.objects.all()
    }))


def edit_user(request, user_id):
    if not request.user.is_superuser:
        return redirect('/login/')

    user = User.objects.get(pk=user_id)

    return render(request, 'cms/user/edit.html', __user_info(request, {
        'form': EditUserForm(
            initial={'id': user_id,
                     'username': user.username,
                     'password': user.password,
                     'email': user.email,
                     'first_name': user.first_name,
                     'last_name': user.last_name,
                     'is_staff': user.is_staff,
                     'is_active': user.is_active
                     })}))


def api_update_user(request):
    if not request.user.is_superuser:
        return redirect('/login/')

    user = User.objects.get(pk=request.POST.__getitem__('id'))
    user.username = request.POST.__getitem__('username')
    user.password = request.POST.__getitem__('password')
    user.email = request.POST.__getitem__('email')
    user.first_name = request.POST.__getitem__('first_name')
    user.last_name = request.POST.__getitem__('last_name')
    user.is_active = request.POST.__getitem__('is_active')

    user.save()

    return HttpResponseRedirect('../user/', __user_info(request, {
        "users": User.objects.all()
    }))


def delete_user(request, user_id):
    if not request.user.is_superuser:
        return redirect('/login/')

    user = User.objects.get(pk=user_id)
    user.delete()

    return HttpResponseRedirect('/cms/user', __user_info(request, {
        "users": User.objects.all()
    }))


def formula_index(request):
    if not request.user.is_superuser:
        return redirect('/login/')

    return render(request, 'cms/formula/index.html', __user_info(request, {
        "formulas": Formula.objects.all(),
    }))


def create_formula(request):
    if not request.user.is_superuser:
        return redirect('/login/')

    return render(request, 'cms/formula/create.html', __user_info(request, {
        'form': EditFormulaForm()
    }))


def api_create_formula(request):
    if not request.user.is_superuser:
        return redirect('/login/')

    formula = Formula(name=request.POST.__getitem__('name'),
                      content=request.POST.__getitem__('content'),)
    formula.save()

    return HttpResponseRedirect('../formula/', __user_info(request, {
        "formulas": Formula.objects.all()
    }))


def edit_formula(request, formula_id):
    if not request.user.is_superuser:
        return redirect('/cms/login/')

    formula = Formula.objects.get(pk=formula_id)

    return render(request, 'cms/formula/edit.html', __user_info(request, {
        'form': EditFormulaForm(initial={'id': formula_id,
                                         'name': formula.name,
                                         'content': formula.content
                                         })}))


def api_update_formula(request):
    if not request.user.is_superuser:
        return redirect('/login/')

    formula = Formula.objects.get(pk=request.POST.__getitem__('id'))
    formula.name = request.POST.__getitem__('name')
    formula.content = request.POST.__getitem__('content')

    formula.save()

    return HttpResponseRedirect('../formula/', __user_info(request, {
        "formula": Formula.objects.all()
    }))


def delete_formula(request, formula_id):
    if not request.user.is_superuser:
        return redirect('/login/')

    formula = Formula.objects.get(pk=formula_id)
    formula.delete()

    return HttpResponseRedirect('/cms/formula', __user_info(request, {
        "formulas": Formula.objects.all()
    }))


# Contest
def contest_index(request):
    if not request.user.is_superuser:
        return redirect('/login/')

    return render(request, 'cms/contest/index.html', __user_info(request, {
        'form': ContestForm(),
    }))


# Move up, down order
def move_up(request, topic_id):
    if not request.user.is_superuser:
        return redirect('/login/')

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
        return redirect('/login/')

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


# TODO: put in the suitable file
# Martinus
# Jan 16, 2016
def format_answer_box(question):
    if question.answer != " ":
        formatted_answer = substitute_answer_with_box(question.id, None, question.respone_type, question.answer, topic=question.concept.topic.name, has_subpart=False)
        setattr(question, "answer", formatted_answer)
        print(question.answer)
    else:
        answer_parts = question.answerpart_set.all()
        for answer in answer_parts:
            answer.part_content = substitute_answer_with_box(answer.id, 0, answer.part_respone_type, answer.part_content, topic=question.concept.topic.name)
            if answer.subpart_name_1 == "i":
                answer.subpart_content_1 = substitute_answer_with_box(answer.id, 1, answer.respone_type_1, answer.subpart_content_1, topic=question.concept.topic.name)
            if answer.subpart_name_2 == "ii":
                answer.subpart_content_2 = substitute_answer_with_box(answer.id, 2, answer.respone_type_2, answer.subpart_content_2, topic=question.concept.topic.name)
            if answer.subpart_name_3 == "iii":
                answer.subpart_content_3 = substitute_answer_with_box(answer.id, 3, answer.respone_type_3, answer.subpart_content_3, topic=question.concept.topic.name)
            if answer.subpart_name_4 == "iv":
                answer.subpart_content_4 = substitute_answer_with_box(answer.id, 4, answer.respone_type_4, answer.subpart_content_4, topic=question.concept.topic.name)
        # Error: 'Question' object does not support item assignment
        # question['answer_parts'] = answer_parts
        setattr(question, "answer_parts", answer_parts)
        try:
            print(answer_parts[0].part_content)
        except IndexError:
            pass
    return question


def substitute_answer_with_box(answerpart_id, subpart_no, answer_type, original_answer, topic="Unknown", has_subpart=True):
    if not has_subpart:
        subpart_no = 'q'
    # Count the number of input in each part
    answer_count = len(re.findall(r'(["])(?:(?=(\\?))\2.)*?\1', original_answer))
    # Remove all answer
    content = re.sub(r'(["])(?:(?=(\\?))\2.)*?\1', '""', original_answer)
    for i in range(answer_count):
        # Construct HTML tag
        if answer_type == "Numberic" or answer_type == "EXPRESSION":
            output_HTML_tag = '<span id="answer-' + str(answerpart_id)   + "-" + str(subpart_no) + \
                "-" + str(i) + '"></span>'
            output_HTML_tag += '<input type="hidden" name="answer-' + str(answerpart_id) + "-" + \
                str(subpart_no) + '"' + 'id="hidden_answer-' + str(answerpart_id) + "-" + \
                str(subpart_no) + "-" + str(i) + '" >'
            # Substitute the answer with HTML tag (process each sub_part one by one)
            if not has_subpart:
                print output_HTML_tag
            content = re.sub(r'""', output_HTML_tag, content, 1)
        elif answer_type == "Text":
            output_HTML_tag = '<input type="text" name="answer-' + str(answerpart_id) + "-" + \
                str(subpart_no) + '"' + 'id="hidden_answer-' + str(answerpart_id) + "-" + str(subpart_no) + "-" + \
                str(i) + '" >'
            # Substitute the answer with HTML tag (process each sub_part one by one)
            content = re.sub(r'""', output_HTML_tag, content, 1)
        elif answer_type == "Prove" and topic == "Trigonometry":
            lhs_question = '$' + 'LHS (under development)' + '$'
            output_HTML_tag = '<div class="row"><div id="col-md-6">'
            output_HTML_tag += lhs_question
            output_HTML_tag += '</div><div id="col-md-6"><div id="answer_container-' + str(answerpart_id) + "-" + str(subpart_no) + '">'
            output_HTML_tag += "<span>= </span>"
            output_HTML_tag += '<span style="min-width:120px; min-height:25px;" id="answer-' + str(answerpart_id) + "-" + str(subpart_no) + \
                              "-" + str(i) + '"></span>'
            output_HTML_tag += '<input type="hidden" name="answer-' + str(answerpart_id) + "-" + \
                               str(subpart_no) + '"' + 'id="hidden_answer-' + str(answerpart_id) + "-" + \
                               str(subpart_no) + "-" + str(i) + '" >'
            output_HTML_tag += '</div>'
            output_HTML_tag += '<div id="answer_button_container-' + str(answerpart_id) + "-" + str(subpart_no) + '">'
            output_HTML_tag += '<div class="col-md-6">'
            output_HTML_tag += '<a style="float:right" href="#" class="btn btn-default" onclick="add_step(' + str(answerpart_id) + ','
            if subpart_no == 'q':
                output_HTML_tag += "'q'"
            else:
                output_HTML_tag += str(subpart_no)
            output_HTML_tag += ')" >Add Steps</a>'
            output_HTML_tag += '</div><div class="col-md-6">'
            output_HTML_tag += '<a style="float:left" href="#" class="btn btn-default" onclick="remove_step(' + str(answerpart_id) + ','
            if subpart_no == 'q':
                output_HTML_tag += "'q'"
            else:
                output_HTML_tag += str(subpart_no)
            output_HTML_tag += ')" >Remove Steps</a>'
            output_HTML_tag += '</div></div></div></div>'
            content = output_HTML_tag
            break
        elif answer_type == "Prove" and topic == "Plane Geometry":
            output_HTML_tag = '<center><div id="answer_container-' + str(answerpart_id) + "-" + str(subpart_no) + '">'
            output_HTML_tag += "<span></span>"
            output_HTML_tag += '<span style="min-width:120px; min-height:25px;" id="answer-' + str(answerpart_id) + "-" + str(subpart_no) + \
                              "-" + str(i) + '"></span>'
            output_HTML_tag += '<input type="hidden" name="answer-' + str(answerpart_id) + "-" + \
                               str(subpart_no) + '"' + 'id="hidden_answer-' + str(answerpart_id) + "-" + \
                               str(subpart_no) + "-" + str(i) + '" >'
            output_HTML_tag += '</div>'
            output_HTML_tag += '<div id="answer_button_container-' + str(answerpart_id) + "-" + str(subpart_no) + '">'
            output_HTML_tag += '<div class="col-md-6">'
            output_HTML_tag += '<a style="float:left" href="#" class="btn btn-default" onclick="remove_step(' + str(answerpart_id) + ','
            if subpart_no == 'q':
                output_HTML_tag += "'q'"
            else:
                output_HTML_tag += str(subpart_no)
            output_HTML_tag += ')" >Remove Steps</a>'
            output_HTML_tag += '</div></div></center>'
            content = output_HTML_tag
            break
        else:
            print(answer_type + " " + topic)
            output_HTML_tag = "Unknown error"
            # Substitute the answer with HTML tag (process each sub_part one by one)
            content = re.sub(r'""', output_HTML_tag, content, 1)
    return content
