from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework import status
from django.core.cache import cache
import requests
import json
from .utils import prepare_actors_data

GHIBLI_DOMAIN = 'https://ghibli.rest'

@api_view(['GET'])
@permission_classes([HasAPIKey | IsAuthenticated])
def list_movies(request):
    # get movie list from cache
    movies = cache.get('movies_list')
    if movies is None:
        result = requests.get(f'{GHIBLI_DOMAIN}/films')
        if(result.text):
            movies = json.loads(result.text)
            for movie in movies:
                    actors_data = []
                    for actors_url in movie.get("people"):                        
                            actors_data = prepare_actors_data(actors_url)

                    movie['actors'] = actors_data
                    movie.pop('people', None)
            cache.set('movies_list', movies, 60)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(movies, status=status.HTTP_200_OK)

