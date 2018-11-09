from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_source,get_source,search_source
from .forms import ReviewForm
from ..models import Review

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting news sources
    Breaking_news = get_source('Breaking news')
    Business_news = get_source('Business')
    General_news = get_source('General')
    title = 'Home - Welcome to The best News Review Website Online'

    search_source = request.args.get('source_query')

    if search_source:
        return redirect(url_for('main.search',source_name=search_source))
    else:
        return render_template('index.html', name = name, Breaking = Breaking_news, Business = Business_news, General = General_news)
# Views
@main.route('/source/<int:id>')
def source(id):

    '''
    View news page function that returns the news details page and its data
    '''

    Source = get_source(id)
    name = f'{source.name}'
    reviews = Review.get_reviews(source.id)
    return render_template('news.html', name = name, source=source,reviews = reviews )

@main.route('/search/<source_name>')
def search(source_name):
    '''
    View function to display the search results
    '''
    source_name_list = source_name.split(" ")
    source_name_format = "+".join(source_name_list)
    searched_news = search_news(source_name_format)
    name = f'search results for {source_name}'
    return render_template('search.html',source = searched_source, name=name)

@main.route('/source/review/news/<int:id>', methods = ['GET','POST'])
def source_review(id):
    form = ReviewForm()
    source = get_source(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(news.id,title,news.poster,review)
        new_review.save_review()
        return redirect(url_for('main.news',id = news.id ))

    title = f'{news.title} review'
    return render_template('new_review.html',title = title, review_form=form, news=news)