import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import urllib.robotparser

def is_allowed_by_robots(base_url, path):
    """
    robots.txt dosyasına göre taramaya izin veriliyor mu?
    """
    parsed_url = urlparse(base_url)
    robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
        return rp.can_fetch("*", path)
    except Exception as e:
        print(f"[robots.txt] Hata: {e}. {path} için varsayılan olarak izin VERİLMEYECEK.")
        return False  # Güvenli yaklaşım: izin verme

def get_all_links(base_url):
    """
    Verilen site içinde aynı domaine ait ve robots.txt'e uygun tüm linkleri toplar.
    """
    try:
        resp = requests.get(base_url, timeout=50)  # timeout 50
        soup = BeautifulSoup(resp.text, "html.parser")
        links = set()

        for a in soup.find_all("a", href=True):
            href = urljoin(base_url, a['href'])
            parsed_href = urlparse(href)

            # Aynı domainde mi?
            if parsed_href.netloc == urlparse(base_url).netloc:
                # robots.txt kontrolü
                if is_allowed_by_robots(base_url, parsed_href.path):
                    links.add(href)
                else:
                    print(f"[robots.txt] Atlanıyor: {href}")
        return list(links)

    except Exception as e:
        print(f"Error fetching links: {e}")
        return []
