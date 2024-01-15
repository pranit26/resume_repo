from django.urls import path
from .views import create_candidate,get_candidate_list,download_resume


urlpatterns = [
       path('create/',create_candidate),
       path('get_candidate_list/',get_candidate_list),
       path('download_resume/',download_resume),
]