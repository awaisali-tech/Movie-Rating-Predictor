import requests
import json

url = "https://ott-details.p.rapidapi.com/advancedsearch"

headers = {
    "x-rapidapi-host": "ott-details.p.rapidapi.com",
    "x-rapidapi-key": "9dd01a5592mshc2deb8ada4c83dep157468jsn1f6ffd1c60c4"
}

# We'll loop over multiple pages to get more data
all_movies = []
for page in range(1, 20):  # change 6 → bigger number if you want more pages
    querystring = {
        "start_year": "1970",
        "end_year": "2020",
        "min_imdb": "6",
        "max_imdb": "7.8",
        "genre": "action",
        "language": "english",
        "type": "movie",
        "sort": "latest",
        "page": str(page)
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    
    # add results from this page
    if "results" in data:
        all_movies.extend(data["results"])
    else:
        break  # stop if no more data

print(f"Total movies fetched: {len(all_movies)}")

# save to json file
with open("movies.json", "w") as f:
    json.dump(all_movies, f, indent=4)

print("Data saved as movies.json")


