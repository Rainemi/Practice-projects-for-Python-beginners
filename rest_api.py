import requests
from pprintpp import pprint
import pandas as pd
api_key = ''


#endpoint/url
#http method to be used
#GET
#/movie/{movie_id}
#https://api.themoviedb.org/3/movie/550?api_key=1543de06632fef3eb79d914b2add2f4c
#to search for the movie /search/movie
#version 3
end_data = []
movie_id = 550
movies = 'avengers'
api_version = 3
api_base_url = f'https://api.themoviedb.org/{api_version}'
endpoint_path = f'/search/movie'
endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}&query={movies}&page=1'
r = requests.get(endpoint)
if r.status_code in range(200,299):
    data = r.json()
    results = data['results']
    movie_ids = set()
    if len(results) > 1:
        for result in results:
            _id = result['id']
            movie_ids.add(_id)
            #print(movie_ids)
for movie_id in movie_ids:
    #movie_id = 550
    movies = 'avengers'
    api_version = 3
    api_base_url = f'https://api.themoviedb.org/{api_version}'
    endpoint_path = f'/search/movie'
    endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}&query={movies}'
    r = requests.get(endpoint)
    
    if r.status_code in range(200,299):
    #data = r.json()
        end_data.append(data)
        #print(end_data)
df = pd.DataFrame(end_data)
df.to_csv('end_data5.csv',index=False)
print(df.head())

#version 4
"""
api_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxNTQzZGUwNjYzMmZlZjNlYjc5ZDkxNGIyYWRkMmY0YyIsInN1YiI6IjYzM2FiODk4MmIxMTNkMDA3YWU4MmUzMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.fNMbwBPBEWSTkQ2zSKFume7zUNAVjLgwIltsTA96Smw'

movie_id = 550
api_version = 4
headers = {
'Authorization' : f'Bearer {api_token}',
'Content-Type' : 'application/json;charset=utf-8'
    }
api_base_url = f'https://api.themoviedb.org/{api_version}'
endpoint_path = f'/movie/{movie_id}'
endpoint = f'{api_base_url}{endpoint_path}'
r = requests.get(endpoint, headers= headers)
print(endpoint)
print(r.status_code)
print(r.json())
"""
