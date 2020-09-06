from django.shortcuts import redirect


def authenticated_user(view_func):
    def wrapper_func(req, *args, **kwargs):
        if req.user.is_authenticated:
            return redirect("home")
        else:
            return view_func(req, *args, **kwargs)
    return wrapper_func
