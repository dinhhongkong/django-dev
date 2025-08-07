from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser

from apps.film.models import Film
from apps.film.serializers import FilmSerializer


# Create your views here.
def film_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        films = Film.objects.all()
        serializer = FilmSerializer(films, many=True)
        return JsonResponse(serializer.data, safe=False)

    return JsonResponse({'error': 'Method not allowed'}, status=405)