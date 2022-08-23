import requests
from time import sleep
from parsel import Selector


# Requisito 1
def fetch(url):
    HEADERS = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, headers=HEADERS, timeout=3)
        sleep(1)
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    links = selector.css(".archive-main h2 a::attr(href)").getall()
    if not links:
        return []
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
