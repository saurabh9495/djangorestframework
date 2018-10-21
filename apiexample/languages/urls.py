from django.urls import path, include
from . import views 
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)
router.register('UpcomingProjects', views.UpcomingProjectView)
router.register('Currents', views.CurrentView)
urlpatterns = [
    path('',include(router.urls))
]