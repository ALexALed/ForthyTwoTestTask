# - *- coding: utf- 8 - *-
__author__ = 'alexaled'


from django.conf import settings


def add_conf_proc(request):
    return {'settings': settings,
            'login_status': request.user.is_authenticated()
            }
