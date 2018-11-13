
from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_articles, get_source
from ..models import Source,Articles

@main.route('/news/<int:news_id>')
def source(source_id):
    return render_template('source.html',id = source_id)  
@main.route('/')
def index():
    #getting categories
    category_news = get_source('general')
    technology = get_source('technology')
    business = get_source('business')
    print(category_news)
    title = 'great news sources here'
    return render_template('index.html',title = title, category_news = category_news, technology = technology, business = business)

@main.route('/articles/articles:category')
def articles(articles_category):
    articles = get_articles(articles_category)
    print(articles)
    title = 'f{articles_category}'

    return render_template('articles.html',id=articles_category,title=title,articles=articles) 
