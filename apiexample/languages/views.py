from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Language, UpcomingProject, Current
from .serializers import LanguageSerializer, UpcomingProjectSerializer, CurrentSerializer

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class UpcomingProjectView(viewsets.ModelViewSet):
    queryset = UpcomingProject.objects.all()
    serializer_class = UpcomingProjectSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class CurrentView(viewsets.ModelViewSet):
    queryset = Current.objects.all()
    serializer_class = CurrentSerializer
    # permission_classes = (permissions.IsAuthenticated,)