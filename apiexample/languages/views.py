from django.shortcuts import render
from rest_framework import viewsets
from .models import Language, UpcomingProject, Current
from .serializers import LanguageSerializer, UpcomingProjectSerializer, CurrentSerializer

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class UpcomingProjectView(viewsets.ModelViewSet):
    queryset = UpcomingProject.objects.all()
    serializer_class = UpcomingProjectSerializer

class CurrentView(viewsets.ModelViewSet):
    queryset = Current.objects.all()
    serializer_class = CurrentSerializer