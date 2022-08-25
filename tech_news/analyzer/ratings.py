from collections import Counter
from tech_news.database import find_news


def sorted_values(news):
    return -news["comments_count"], news["title"]


# Requisito 10
def top_5_news():
    top_5 = list()
    list_news = find_news()
    sorted_list = sorted(list_news, key=sorted_values)
    for news in sorted_list[:5]:
        top_5.append((news["title"], news["url"]))

    return top_5


def sort_list_categories(list_news):
    list_caterogies = list()
    for new in list_news:
        list_caterogies.append(new["category"])
    sorted_list_categories = sorted(list_caterogies)
    counter_list_categories = Counter(sorted_list_categories).most_common()
    return counter_list_categories


def list_categories(counter_caterogies):
    list_categories = list()
    for category, __count__ in counter_caterogies:
        list_categories.append(category)
    return list_categories


# Requisito 11
def top_5_categories():
    list_news = find_news()
    dict_list_caterogies = sort_list_categories(list_news)
    top_5_list_categories = list_categories(dict_list_caterogies)

    return top_5_list_categories
