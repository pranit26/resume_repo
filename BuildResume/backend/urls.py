from .views import dummy_view
from django.urls import path

urlpatterns = [
    path('dummy/', dummy_view, name='dummy-view'),
]