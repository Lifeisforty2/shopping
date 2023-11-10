"""
URL configuration for shopping_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth  import views as auth_views
<<<<<<< HEAD
from shop.views import logout_view
=======
from shop.views import home_view
from django.contrib.auth.views import LogoutView
>>>>>>> 796bd902aeab841c3926976a4886b744bd086395

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", home_view, name="home"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
<<<<<<< HEAD
    path('logout/', logout_view, name='logout'),
=======
    path("logout/", LogoutView.as_view(), name="logout"),
>>>>>>> 796bd902aeab841c3926976a4886b744bd086395
    #...

]
