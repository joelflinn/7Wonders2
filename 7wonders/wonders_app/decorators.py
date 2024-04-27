from django.http import HttpResponse
from django.shortcuts import redirect

#create a decorator for
# pass in list of roles
def allowed_users(allowed_roles=[]):

    #decorator is placed on top of view
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            print('role', allowed_roles)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('you are not authorized to view this page')
        return wrapper_func
    return decorator