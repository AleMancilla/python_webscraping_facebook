from cProfile import run
from pickle import TRUE
from flask import Flask


import os
import matplotlib.pyplot as plt
from facebook_scraper import get_posts



app = Flask(__name__)

@app.route('/')
def index():
    return "Hola Mundoasdasdadd"


@app.route('/web_scraping/facebook_page/<url_page>')
def web_scraping_facebook_page(url_page):
    print('################ web_scraping_facebook_page ##################')
    posts = []
    print('################ web_scraping_facebook_page1 ##################')
    for post in get_posts(url_page,pages=5, options = {'comments':True,"reactors": True}):
        posts.append(post)
    print('################ web_scraping_facebook_page2 ##################')
    return posts

@app.route('/web_scraping/facebook_page/<url_page>/<int:nro_posts>')
def web_scraping_facebook_page_and_nro_post(url_page,nro_posts):
    print('################ web_scraping_facebook_page_and_nro_post ##################')
    posts = []
    for post in get_posts(url_page,pages=nro_posts, options = {'comments':True,"reactors": True}):
        posts.append(post)
    return posts

if __name__ == '__main__':
    app.run(debug=True, port=5000)

