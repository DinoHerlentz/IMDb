from imdb import IMDb
import time


moviesDB = IMDb()
query = input("Enter movie name : ")
movies = moviesDB.search_movie(query)

"""
for movie in movies:
    title = movie['title']
    year = movie['year']
    print(f"{title} - {year}")
"""

id = movies[0].getID()
movie = moviesDB.get_movie(id)

title = movie['title']
year = movie['year']
rating = movie['rating']
# directors = movie['directors']
casting = movie['cast']

print(f"Movie Info - {query.title()}")
print(f"Movie Name : {title}")
print(f"Movie Year : {year}")
print(f"Rating : {rating}")

# direcStr = " ".join(map(str, directors))
# print(f"Directors : {direcStr}")

actors = ", ".join(map(str, casting))
print(f"Actors : {actors}")
