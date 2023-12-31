"""
URL configuration for not_service project.

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
from rest_framework import routers

from mailing_app.views import ClientViewSet, MessageViewSet, MailingViewSets
from .yasg import swaggerurlpatterns

Router = routers.DefaultRouter()
Router.register(r'clients', ClientViewSet)
Router.register(r'message', MessageViewSet)
Router.register(r'mailing', MailingViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(Router.urls)),
    path('api-auth', include('rest_framework.urls'))
]

urlpatterns += swaggerurlpatterns