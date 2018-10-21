from rest_framework import serializers
from .models import Language, UpcomingProject, Current

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ( 'id', 'url', 'name', 'paradigm')

class UpcomingProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UpcomingProject
        fields = ('id', 'url', 'framework', 'programmer')

class CurrentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Current
        fields = ('id', 'url', 'frontend', 'backend')

        