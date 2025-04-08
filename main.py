import csv
import requests
from bs4 import BeautifulSoup
from itertools import zip_longest
from urllib.parse import quote_plus



search_query = input("What job are you looking for? ") #python-devloper
encoded_query = quote_plus(search_query) #python+developer


# pretend you are a real browser to prevent blocking
headers = {
    "User-Agent": "Mozilla/5.0"  
}


url = f"https://wuzzuf.net/search/jobs/?q={encoded_query}"
result = requests.get(url)