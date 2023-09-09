from rest_framework import viewsets
from django.http import HttpResponse
from bs4 import BeautifulSoup
import re
import requests

def unescape_html(text):
    html_entities = [
        ('&lt;', '<'),
        ('&gt;', '>'),
        ('&quot;', '"'),
        ('&#39;', "'"),
        ('&amp;', '&')
    ]
    for entity, char in html_entities:
        text = text.replace(entity, char)
    return text

class UnlockerViewSet(viewsets.ViewSet):
    def retrieve(self, request):
        url = request.GET.get('url', '')
        if not url:
            return HttpResponse("<h1>Please pass a <strong>url</strong> in the query param </h1>", content_type="text/html")

        try:
            response = requests.get(f"http://webcache.googleusercontent.com/search?q=cache:{url}&strip=0&vwsrc=1&&hl=en&lr=lang_en")
            response.raise_for_status()

            data = response.text
            soup = BeautifulSoup(data, 'html.parser')

            pre_tags = soup.find_all('pre')

            if not pre_tags:
                return HttpResponse("<h1>No data found.</h1>", content_type="text/html")

            text_data = pre_tags[0].get_text()
            text_data = unescape_html(text_data)

            text_data = re.sub(r'<script[^>]*>(.*?)<\/script>', '', text_data).strip()

            return HttpResponse(text_data, content_type="text/html")
        except Exception as e:
            print(e)
            return HttpResponse("<h1>Invalid URL or No Data found</h1>", content_type="text/html")
