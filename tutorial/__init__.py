from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def post_element(request):
    {"test":"done"}
    serializer = {"test":"done"}
    return JsonResponse(serializer,safe=False)
