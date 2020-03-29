from django.shortcuts import render
from . import models
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus

BASE_URL = 'https://www.google.com/search?q={}&oq=hello+&aqs=chrome..69i57j46j0j46j0l4.1449j0j7&sourceid=chrome&ie=UTF-8'
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent" : USER_AGENT}

def home(request):
    return render(request, 'base.html')

def new_search(request):
    searched = request.POST.get('search')
    models.Search.objects.create(search=searched)
    print(searched)
    final_url = BASE_URL.format(quote_plus(searched))
    print(final_url)
    resp = requests.get(final_url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    #print(soup.prettify())

    final_search_list = []

    search_list = soup.find_all('div', {'class': 'rc'})


    for search in search_list:

        search_title = search.find(class_="LC20lb DKV0Md").text
        search_desc = search.find(class_="st").text
        search_link = search.find('a').get('href')

        final_search_list.append((search_title, search_desc,search_link))

    #print(soup.find_all('div', {'class': 'g'}))
    #print(soup.find_all('div', {'class': 'rc'}))

    stuff_for_front_end = {
        'searched': searched,
        'final_search_list': final_search_list,

    }
    return render(request, 'home_app/new_search.html',stuff_for_front_end)
