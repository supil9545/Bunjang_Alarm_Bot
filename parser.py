import requests
from bs4 import BeautifulSoup
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websaver.settings")

import django
django.setup()

from parsed_data.models import BlogData

def parse_blog():
    req = requests.get('https://beomi.github.io/beomi.github.io_old/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select(
        'h3 > a'
    )
    data = {}

    for title in my_titles:
        data[title.text] = title.get('href')

    return data

if __name__=='__main__':
    blog_data_dict = parse_blog()
    for t, l in blog_data_dict.items():
        BlogData(title = t, link = l).save()
