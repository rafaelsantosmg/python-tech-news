from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news_title_list = list()
    list_news = search_news({"title": {"$regex": title, "$options": "i"}})
    for new in list_news:
        news_title_list.append((new["title"], new["url"]))

    return news_title_list


# Requisito 7
def search_by_date(date):
    try:
        news_date = list()
        date_parse = datetime.strptime(date, "%Y-%m-%d")
        date_string = datetime.strftime(date_parse, "%d/%m/%Y")
        list_news_date = search_news({"timestamp": date_string})
        for date_news in list_news_date:
            news_date.append((date_news["title"], date_news["url"]))
    except ValueError:
        raise ValueError("Data inválida")
    return news_date


# Requisito 8
def search_by_tag(tag):
    news_tag = list()
    list_news_tags = search_news({"tags": {"$regex": tag, "$options": "i"}})
    for tags_news in list_news_tags:
        news_tag.append((tags_news["title"], tags_news["url"]))
    return news_tag


# Requisito 9
def search_by_category(category):
    news_category = list()
    list_news_categorys = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )
    for categories_news in list_news_categorys:
        news_category.append(
            (categories_news["title"], categories_news["url"])
        )
    return news_category
