from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied

user = get_user_model()


def check_for_permission(function):
    def wrap(request, *args, **kwargs):
        if not request.user.role == 'ADMIN':
            return function(request, *args, *kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

