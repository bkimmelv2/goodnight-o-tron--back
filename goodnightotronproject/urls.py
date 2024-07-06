"""
URL configuration for goodnightotronproject project.

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
from goodnightotron.views import BookViewSet, NoteViewSet, RandomView

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router2 = routers.DefaultRouter()
router2.register(r'notes', NoteViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include(router2.urls)),
    path('admin/', admin.site.urls),
    path('random/', RandomView.as_view())
]
