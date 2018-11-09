from flask import render_template,request,redirect,url_for

from ..request import get_sources,get_article

from . import main


@main.route('/')
def index():
    """
    Function that returns the index page and all its data
    """
    entertainment_news = get_sources('entertainment')
    sport_news = get_sources('sports')
    tech_news = get_sources('technology')
    title = title
    
    return render_template('index.html', title=title, sports=sport_news, technology=tech_news, entertainment=entertainment_news)


@main.route('/source/<id>')
def articles(id):
    """
    View articles
    """
    article = get_article(id)
    print(article)
    title = f'News{id}'
    return render_template('news.html', title=title, article=article)