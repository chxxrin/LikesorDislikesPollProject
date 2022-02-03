from django.urls import path
from .views import *

urlpatterns = [

    path('', start_page, name = "start_page"),

    path('main_page', main_page, name = "main_page"),

    path('vote_page', vote_page, name = "vote_page"),

    path('vote/result', vote, name = "vote"),

    path('vote_result/<int:type_pk>', vote_result, name = "vote_result"),

]
