from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *


class ChoiceAdmin(admin.ModelAdmin):
    fields = ['choice_text', 'votes']

admin.site.register(Choice)
admin.site.register(Vote)
admin.site.unregister(Group)