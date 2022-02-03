from django.forms.models import ModelForm
from django import forms
from .models import Vote, Choice

class Voteform(ModelForm):
    class Meta:
        model = Vote
        fields = ['vote_name']

class Choiceform(ModelForm):
    class Meta:
        model = Choice
        fields = ['name', 'count', 'powerful']

