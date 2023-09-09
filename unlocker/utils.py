from bs4 import BeautifulSoup
from django.urls import reverse

def update_links_to_proxy(soup: BeautifulSoup, is_api: bool=False):
    """Modify all anchor tags in the soup to route through the viewset."""
    for a_tag in soup.find_all('a', href=True):
        original_link = a_tag['href']
        proxy_url = reverse(f"data-{'api' if is_api else 'retrieve'}") + f"?url={original_link}"
        a_tag['href'] = proxy_url
    return soup
