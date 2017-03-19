from apiv2.models import KeyPoint


def update_keypoint(keypoint_data):
    try:
        keypoint_obj = KeyPoint.objects.get(id=keypoint_data.get(u'id'))
        content = keypoint_data.get(u'content')
        keypoint_obj.content = content

        keypoint_obj.save()

        return keypoint_obj
    except KeyPoint.DoesNotExist:
        return False