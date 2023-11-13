import requests
from django.core.cache import cache
import json


def prepare_actors_data(actors_url):
    actors_data = cache.get(f"actors_{actors_url}") 
    if actors_data is None:
        actors_result = requests.get(actors_url)
        if(actors_result.text):
            actors_data = [{'id':actor['id'],
                        'name':actor['name'],
                        'species':actor['species'],
                        'url':actor['url']} for actor in json.loads(actors_result.text)]
            # caching people data for 24 hours since different movies can have same set of people
            cache.set(f"actors_{actors_url}", actors_data, 60*60*24)
    return actors_data or []