"""platzigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from platzigram import views as local_views
from posts import views as post_views

from django.conf.urls.static import static
from django.conf import settings

from users import views as users_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',local_views.hello, name='hello_word'),
    path('sorted/', local_views.sorted, name='sort'),
    path('hi/<str:name>/<int:age>/', local_views.hi, name='hi'),

    #POSTS

    path('', post_views.list_views, name='feed'),
    path('posts/new', post_views.create_post, name='create_post'),

    #Users
    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
    path('users/signup/', users_views.signup, name="signup" ),
    path('users/update', users_views.update_profile, name="update_profile"), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


