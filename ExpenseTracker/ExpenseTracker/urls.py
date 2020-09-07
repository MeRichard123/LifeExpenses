from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views as account_views

urlpatterns = [
<<<<<<< HEAD
    path("admin/", admin.site.urls),
=======
    path('admin/', admin.site.urls),
>>>>>>> 73a66e842e2456b6653eefdd7112a3bfc3337f9d
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    path("register/", account_views.register, name="register"),

    path("", include("accounts.urls")),
    path("", include("expense.urls")),
<<<<<<< HEAD
    path("", include("todo.urls"))
=======
    path('todo/', include('todo.urls'))
>>>>>>> 73a66e842e2456b6653eefdd7112a3bfc3337f9d
]
