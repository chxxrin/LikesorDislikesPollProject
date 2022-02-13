from django.urls import path
from .views import *
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [

    path('', start_page, name = "start_page"),

    path('main_page', main_page, name = "main_page"),

    path('vote_page', vote_page, name = "vote_page"),

    path('vote/result', vote, name = "vote"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
