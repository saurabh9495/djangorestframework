from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class UpcomingProject(models.Model):
    framework = models.CharField(max_length=50)
    programmer = models.CharField(max_length=50)
    
    def __str__(self):
        return self.framework

class Current(models.Model):
    frontend = models.CharField(max_length=50)
    backend = models.CharField(max_length=50)

    def __str__(self):
        return self.frontend