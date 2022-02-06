from django.urls import path
from .views import *

urlpatterns = [

    path('', start_page, name = "start_page"),

    path('main_page', main_page, name = "main_page"),

    path('vote_page', vote_page, name = "vote_page"),

    path('vote/result', vote, name = "vote"),

    path('vote_result/<int:type_pk>/<int:user_type>/<int:c1>/<int:c2>/<int:c3>/<int:c4>/<int:c5>/<int:c6>/<int:c7>/<int:c8>/<int:c9>/<int:c10>/', vote_result, name = "vote_result"),
]
