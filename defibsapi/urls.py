"""defibsapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers

from contributors.views import ContributorViewSet
from defibs.views import DefibViewSet

router = routers.DefaultRouter()
router.register(r'contributors', ContributorViewSet, base_name='contributor')
router.register(r'defibs', DefibViewSet, base_name='defib')

urlpatterns = [
    path(r'', include(router.urls)),
    path('admin/', admin.site.urls),
]
