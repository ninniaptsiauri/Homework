import json

with open('Homework 19/movies.json', 'r') as json_file:
    try:
       movies = json.load(json_file)
    except json.decoder.JSONDecodeError as e:
        print(e)

sorted_movies = []

for movie in movies:
    for movie1 in movie['results']:
        release_year = int(movie1['release_date'][:4])
        if release_year > 2000 and 'Crime' in movie1['genres']:
            movie1['genres'] = ['New_Crime' if genre == 'Crime' else genre for genre in movie1['genres']] 
            sorted_movies.append(movie1)

        elif release_year < 2000 and 'Drama' in movie1['genres']:
            movie1['genres'] = ['Old_Drama' if genre == "Drama" else genre for genre in movie1['genres']]
            sorted_movies.append(movie1)

        elif release_year == 2000:
            movie1['genres'].append('New_Century')
            sorted_movies.append(movie1)
                

                
with open('Homework 19/movies.json', 'w') as json_file:
    try:
        json.dump(sorted_movies, json_file, indent=4)
    except IOError as e:
        print(e)
                