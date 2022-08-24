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
    news = selector.css(".archive-main h2 a::attr(href)").getall()
    if not news:
        return []
    return news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_link = selector.css(".next.page-numbers ::attr(href)").get()
    if not next_page_link:
        return None

    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    comments_count = selector.css(".title-block::text").re(r"\d comments")
    return {
        "url": selector.css("head link[rel=canonical]::attr(href)").get(),
        "title": selector.css(".entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".author a::text").get(),
        "comments_count": 0
        if len(comments_count) == 0
        else int(comments_count[0][0]),
        "summary": "".join(
            selector.css(".entry-content > p:nth-of-type(1) *::text").getall()
        ).strip(),
        "tags": selector.css(".post-tags ul li a::text").getall(),
        "category": selector.css(".label::text").get(),
    }


# Requisito 5
#     test = list(news)
# test = dict()
def get_tech_news(amount):
    html = fetch("https://blog.betrybe.com/")
    next_link = scrape_next_page_link(html)
    count = 0
    pull_news = list()
    while next_link and count < amount:
        list_news = scrape_novidades(next_link)
        for news in list_news:

            print(scrape_noticia(html))
            pull_news.extend(scrape_noticia(html))
            next_link = scrape_next_page_link(html)
            count += 1

    # for new in range(amount):
    #     links_news = scrape_novidades(html)
    # news = scrape_noticia(fetch(links_news[0]))
    print(pull_news)


get_tech_news(5)
