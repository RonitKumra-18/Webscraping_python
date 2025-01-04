'''from bs4 import BeautifulSoup
import requests
#To filter out
#Requests information from a specific website
html_text = requests.get('https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm').text
#Creating an instance of soup
soup = BeautifulSoup(html_text, 'lxml')
#find the class name of the card(class, classname)
film_names = soup.find_all('div', class_='sc-35aa5141-3 bnEgLu ipc-page-grid__item ipc-page-grid__item--span-2')
for film_name in film_names:
    ratings = film_name.find('span', class_='ipc-rating-star--rating').span.text
    if ratings > 7:
        _name_ = film_name.find('a', class_='ipc-title-link-wrapper').text.replace(' ','')
        year =  film_name.find('span', class_='sc-300a8231-7 eaXxft cli-title-metadata-item').text.replace(' ','')
        lenght_= film_name.find('span', class_='sc-300a8231-7 eaXxft cli-title-metadata-item')
        print(f"name: {_name_} \n")
        print(f"year: {year} \n")
''''''
from bs4 import BeautifulSoup
import requests

# Request information from IMDb's "Most Popular Movies" page
url = 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'
response = requests.get(url)
html_text = response.text

# Create a BeautifulSoup instance
soup = BeautifulSoup(html_text, 'lxml')

# Extract all movies in the chart
movies = soup.select('td.titleColumn')  # Adjust the selector to match IMDb's structure

for movie in movies:
    try:
        # Extract the movie name
        name = movie.a.text.strip()
        
        # Extract the release year
        year = movie.span.text.strip('()')
        
        # Extract the rating (if available)
        rating_cell = movie.find_next('td', class_='ratingColumn imdbRating')
        rating = float(rating_cell.strong.text.strip()) if rating_cell.strong else None
        
        # Print movies with a rating greater than 7
        if rating and rating > 7:
            print(f"Name: {name}")
            print(f"Year: {year}")
            print(f"Rating: {rating}\n")
    except Exception as e:
        # Handle any unexpected issues gracefully
        print(f"Error processing a movie: {e}")
'''
from bs4 import BeautifulSoup
import requests

# Request the IMDb page
url = 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'
head1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}
response = requests.get(url, headers=head1)

if response.status_code == 200:
    html_text = response.text

    # Debug: Print a snippet of the HTML to verify content
    print(html_text[:500])  # Check if the page content is retrieved successfully

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_text, 'lxml')

    # Adjust selectors based on current IMDb page structure
    movies = soup.select('td.titleColumn')  # Update selector if needed

    # Loop through each movie
    for movie in movies:
        try:
            name = movie.a.text.strip()  # Extract movie name
            year = movie.span.text.strip('()')  # Extract year

            # Find the corresponding rating
            rating_cell = movie.find_next('td', class_='ratingColumn imdbRating')
            rating = float(rating_cell.strong.text.strip()) if rating_cell and rating_cell.strong else None

            if rating and rating > 7:  # Only print movies with ratings > 7
                print(f"Name: {name}")
                print(f"Year: {year}")
                print(f"Rating: {rating}\n")
        except Exception as e:
            print(f"Error processing a movie: {e}")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
