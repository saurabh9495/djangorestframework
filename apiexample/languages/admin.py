from django.contrib import admin
from .models import Language, UpcomingProject, Current

admin.site.register(Language)
admin.site.register(UpcomingProject)
admin.site.register(Current)
