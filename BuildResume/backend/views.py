from django.shortcuts import render
from django.http import JsonResponse

def dummy_view(request):
    return JsonResponse({'message': 'This is a dummy view'})