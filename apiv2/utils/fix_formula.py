from apiv2.models import Question


def get_question_from_id(qid):
    q = Question.objects.get(pk=qid)
    return q.content


def set_question_content(qid, new_content):
    q = Question.objects.get(pk=qid)
    q.content = new_content
    q.save()
