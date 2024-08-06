"""
URL configuration for backend_lab project.

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
from django.urls import path
from users.views import (
    first_view,
    second_view,
    subjects_view,
    add_subjects_view,
    update_subjects_view,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', first_view, name="first-view"),
    path('users2/', second_view, name="second-view"),
    path('subjects/', subjects_view, name="subjects-view"),
    path('subjects/add/', add_subjects_view, name="add-subjects-view"),
    path('subjects/update/<int:subject_id>/', update_subjects_view, name="update-subjects-view"),
]
