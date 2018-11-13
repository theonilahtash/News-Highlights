import urllib.request,json
from .models import Source
from .models import Articles
from . import main

# News = news.News
# Articles = articles.Articles
#Getting api key
api_key = None

#Getting the news base url
# base_url = None 
base_url='https://newsapi.org/v2/sources?&category={}&apiKey={}'

#Getting the articles base url
base2_url ='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
def configure_request(app):
    global api_key
    api_key = app.config['SOURCE_API_KEY']
    print(api_key)

def get_source(category):
    get_source_url = base_url.format(category, api_key)
    print(get_source_url)

    with urllib.request.urlopen(get_source_url)as url:
        get_source_data = url.read()
        print(get_source_data)
        get_source_response =json.loads(get_source_data)
        
        source_result = None

        if get_source_response["sources"]:
            news_source_list = get_source_response["sources"]
            source_result = process_source(news_source_list)

    return source_result

def process_source(source_list):
    
    source_results=[]
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        if url:
            source_object = Source(id,name,description,url,category,language,country)
            source_results.append(source_object)

    return source_results

def get_articles(category_news):
    get_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(
        category_news, api_key)
    print(get_articles_url)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        print(get_articles_data)

        get_articles_response =json.loads(get_articles_data)
        
        
        articles_results = None

        if get_articles_response["articles"]:
            articles_results_list = get_articles_response["articles"]
            articles_results = process_articles(articles_results_list)

    return articles_results


def process_articles(articles_list):
    articles_results=[]
    for article in articles_list:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        image = article.get('urlToImage')
        time = article.get('publishedAt')
        if title:
            articles_object = Articles(author,title,description,url,image,time)
            articles_results.append(articles_object)

    return articles_results  

def search_source(source_name):
    search_source_url =  'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    with urllib.request.urlopen(search_source_url) as url:
        search_source_data = url.read()
        print(search_source_data)
        search_source_response = json.loads(search_source_data)

        search_source_results = None

        if search_source_response['results']:
            search_source_list = search_source_response['results']
            # search_source_results = process_results(search_source_list)   

    return search_source_results 
