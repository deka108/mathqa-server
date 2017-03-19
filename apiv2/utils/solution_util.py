from apiv2.models import Solution


def update_solution(solution_data):
    try:
        solution_obj = Solution.objects.get(id=solution_data.get(u'id'))
        content = solution_data.get(u'content')
        solution_obj.content = content

        solution_obj.save()

        return solution_obj
    except Solution.DoesNotExist:
        return False