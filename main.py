import csv
import requests
from bs4 import BeautifulSoup
from itertools import zip_longest
from urllib.parse import quote_plus



search_query = "python developer" 
encoded_query = quote_plus(search_query)


# pretend you are a real browser to prevent blocking
headers = {
    "User-Agent": "Mozilla/5.0"  
}


url = f"https://wuzzuf.net/search/jobs/?q={encoded_query}"
print(url)
result = requests.get(url)


# page markup
src = result.content


# soup object to parse page content (lxml ==> parser)
soup = BeautifulSoup(src, "lxml")


# find all returns list
# tag is written between ""
# attribute is written as a dictionary
job_titles = soup.find_all("h2", {"class":"css-m604qf"})
company_names = soup.find_all("a", {"class":"css-17s97q8"})
companies_locations = soup.find_all("span", {"class":"css-5wys0k"})
job_skills = soup.find_all("div",{"class":"css-y4udm8"})


def print_lst(lst):
    for i in lst:
        print(i)

def extract_text(lst):
    text_lst = []
    for i in range(len(lst)):
        text_lst.append(lst[i].text)
    return text_lst


# extract text from content
job_titles = extract_text(job_titles)  
company_names = extract_text(company_names)
companies_locations = extract_text(companies_locations)
job_skills = extract_text(job_skills)