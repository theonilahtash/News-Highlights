class Source:
    '''
    Source class to define News Objects
    '''

    def __init__(self,id,name,description,poster,category,language,country):
        self.id: time,
        self.name: Time,
        self.description: Breaking news and analysis from TIME.com. Politics, world news, photos, video, tech reviews, health, science and entertainment news,
        self.poster: http://time.com,
        self.category: general,
        self.language: en,
        self.country: us


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