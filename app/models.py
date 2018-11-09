class Source:
    '''
    Source class to define News Objects
    '''

    def __init__(self,id,name,description,url,category,language,country):
        id: time,
        name: Time,
        description: Breaking news and analysis from TIME.com. Politics, world news, photos, video, tech reviews, health, science and entertainment news,
        url: http://time.com,
        category: general,
        language: en,
        country: us


class Articles:

    all_articles = []

    def __init__(self,news_id,name,imageurl,article):
        self.news_id = news_id
        self.name = name
        self.imageurl = imageurl
        self.articles = articles


    def save_article(self):
        Article.all_articles.append(self)


    @classmethod
    def clear_articles(cls):
        Article.all_articles.clear()

    @classmethod
    def get_articles(cls,id):

        response = []

        for article in cls.all_article:
            if article.news_id == id:
                response.append(article)

        return response