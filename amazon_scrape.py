from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Headers for request
HEADERS = ({'User-Agent' : agent, 'Accept-Language': 'en-US, en;q=0.5'})

url = "https://www.imdb.com/chart/top/"

response = requests.get(url, headers=HEADERS)
print(response)

soup = BeautifulSoup(response.content, 'html.parser')
#print(soup)

movies_tags = soup.find_all('div', attrs={'class':"sc-1e00898e-0 jyXHpt cli-children"})
# print(movies_tags[0])
# print("done")

test_movie = movies_tags[0]

print(test_movie.find('h3', attrs={'class':"ipc-title__text"}).text)
print(test_movie.find('div', attrs={'class':"sc-1e00898e-7 hcJWUf cli-title-metadata"}).span.text)
print(test_movie.find('span', attrs={'class':"ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"}).text)
print(test_movie.find('span', attrs={'class':"ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"}).text.split()[0])
print(test_movie.find('span', attrs={'class':"ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"}).text.split()[1][1:-1])


ranks = []
titles = []
years = []
ratings = []
vote_counts = []

for movie_tag in soup.find_all('div', attrs={'class':"sc-1e00898e-0 jyXHpt cli-children"}):
    rank = movie_tag.find('h3', attrs={'class':"ipc-title__text"}).text.split('.')[0]
    title = movie_tag.find('h3', attrs={'class':"ipc-title__text"}).text.split('.', 1)[1]
    year = movie_tag.find('div', attrs={'class':"sc-1e00898e-7 hcJWUf cli-title-metadata"}).span.text
    rating = movie_tag.find('span', attrs={'class':"ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"}).text.split()[0]
    vote_count = movie_tag.find('span', attrs={'class':"ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"}).text.split()[1][1:-1]

    ranks.append(rank)
    titles.append(title)
    years.append(year)
    ratings.append(rating)
    vote_counts.append(vote_count)



# Creating a DataFrame
data = {'Rank': ranks, 'Title': titles, 'Year': years, 
        'Rating':ratings, 'Vote_count':vote_counts}
df = pd.DataFrame(data)

df.to_csv("IMDb_Top_250_Movies_data.csv", index=False)

# Displaying the DataFrame
print(df.head())
print(df.shape)
