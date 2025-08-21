import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_all_links(base_url):
    """
    Verilen site içinde aynı domaine ait tüm linkleri toplar.
    """
    try:
        resp = requests.get(base_url, timeout=10)
        soup = BeautifulSoup(resp.text, "html.parser")
        links = set()
        for a in soup.find_all("a", href=True):
            href = urljoin(base_url, a['href'])
            if urlparse(href).netloc == urlparse(base_url).netloc:
                links.add(href)
        return list(links)
    except Exception as e:
        print(f"Error fetching links: {e}")
        return []
