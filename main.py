import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]
#
# print(f"movies: {movies}\n"
#       f"length: {len(movies)}\n")

with open("movies.txt", mode="w", encoding='utf-8') as file:
    for movie in movies:
        file.write(f"{movie}\n")

# f = open("movies.txt", "w",encoding='utf-8')
# for idx, movie in enumerate(movies):
#     if idx != 58:
#         f.write(f"{movie}\n")
#         print(f"index: {idx}\n")
#         print(f"movie: {movie}\n")
#     else:
#         f.write(f"{movie}\n")
# f.close()

'''
FAQ: Empire's website has changed!

When this lesson was created, I used this URL for the project: 
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

However, Empire has since changed their website. You can see this when you inspect the movie title elements. 
You'll see that the h3 with the class "title" is no longer there. 
To use exactly the same code as per the solution, we can use a cached version of the website from the Internet Archive's Wayback Machine.

'''