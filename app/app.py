from cProfile import run
# from crypt import methods
from pickle import TRUE
from flask import Flask, render_template,request
from flask_mysqldb import MySQL


import os
import matplotlib.pyplot as plt
from facebook_scraper import get_posts


app = Flask(__name__)
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'flask_facebook'

mysql = MySQL(app)



@app.route('/')
def index():
    
    cur = mysql.connection.cursor()
    cur.execute('select * from `fb_emp3`')
    data = cur.fetchall()
    print(data)
   # mysql.connection.commit()
    return render_template('index.html', posts = data)


@app.route('/web_scraping/facebook_page/<url_page>')
def web_scraping_facebook_page(url_page):
    posts = []
    for post in get_posts(url_page,pages=5, options = {'comments':True,"reactors": True}):
        posts.append(post)
    return posts

@app.route('/web_scraping/facebook_page/<url_page>/<int:nro_posts>')
def web_scraping_facebook_page_and_nro_post(url_page,nro_posts):
    posts = []
    for post in get_posts(url_page,pages=nro_posts, options = {'comments':True,"reactors": True}):
        posts.append(post)
    return posts

@app.route('/facebook_scraping_post', methods=['POST'])
def facebook_scraping_post():
    # cur.execute('INSERT INTO fb_emp3 VALUES(2252600314895487)')
    if request.method == 'POST':
        linkUrl = request.form['link_facebook']
        posts = []
        for post in get_posts(post_urls=[linkUrl], options = {'comments':True,"reactors": True}):
            posts.append(post)
            print('###############################################################')
            print(post)
            print('###############################################################')
            post_id = post['post_id']
            text = str(post['text'])
            post_text = str(post['post_text'])
            shared_text =str( post['shared_text'])
            original_text = post['original_text']
            time = post['time']
            timestamp = post['timestamp']
            image = str(post['image'])
            image_lowquality = str(post['image_lowquality'])
            images = str(post['images'])
            images_description = str(post['images_description'])
            images_lowquality = str(post['images_lowquality'])
            images_lowquality_description = str(post['images_lowquality_description'])
            video = str(post['video'])
            video_duration_seconds = post['video_duration_seconds']
            video_height = post['video_height']
            video_id = post['video_id']
            video_quality = post['video_quality']
            video_size_MB = post['video_size_MB']
            video_thumbnail = str(post['video_thumbnail'])
            video_watches = post['video_watches']
            video_width = post['video_width']
            likes = post['likes']
            comments = post['comments']
            shares = post['shares']
            post_url = str(post['post_url'])
            link = str(post['link'])
            links = str(post['links'])
            user_id = post['user_id']
            username = str(post['username'])
            user_url = str(post['user_url'])
            is_live = str(post['is_live'])
            factcheck = post['factcheck']
            shared_post_id = post['shared_post_id']
            shared_time = post['shared_time']
            shared_user_id = post['shared_user_id']
            shared_username = str(post['shared_username'])
            shared_post_url = str(post['shared_post_url'])
            available = str(post['available'])
            comments_full = str(post['comments_full'])
            reactors = post['reactors']
            w3_fb_url = post['w3_fb_url']
            reactions = post['reactions']
            reaction_count = post['reaction_count']
            with_ = str(post['with'])
            page_id = post['page_id']
            sharers = post['sharers']
            image_id = post['image_id']
            image_ids = str(post['image_ids'])
            # was_live = str(post['was_live'])
            # header = str(post['header'])
            
            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO `fb_emp3` (`post_id`, `text`, `post_text`, `shared_text`, `original_text`, `time`, `timestamp`, `image`, `image_lowquality`, `images`, `images_description`, `images_lowquality`, `images_lowquality_description`, `video`, `video_duration_seconds`, `video_height`, `video_id`, `video_quality`, `video_size_MB`, `video_thumbnail`, `video_watches`, `video_width`, `likes`, `comments`, `shares`, `post_url`, `link`, `links`, `user_id`, `username`, `user_url`, `is_live`, `factcheck`, `shared_post_id`, `shared_time`, `shared_user_id`, `shared_username`, `shared_post_url`, `available`, `comments_full`, `reactors`, `w3_fb_url`, `reactions`, `reaction_count`, `with`, `page_id`, `sharers`, `image_id`, `image_ids`, `was_live`, `header`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(post_id,text,post_text,shared_text,original_text,time,timestamp,image,image_lowquality,images,images_description,images_lowquality,images_lowquality_description,video,video_duration_seconds,video_height,video_id,video_quality,video_size_MB,video_thumbnail,video_watches,video_width,likes,comments,shares,post_url,link,links,user_id,username,user_url,is_live,factcheck,shared_post_id,shared_time,shared_user_id,shared_username,shared_post_url,available,comments_full,reactors,w3_fb_url,reactions,reaction_count,with_,page_id,sharers,image_id,image_ids,'was_live','header'))
            mysql.connection.commit()
    #     print(linkUrl)
    return 'Los datos se cargaron a la base de datos correctamente, porfavor vuelve al inicio'

@app.route('/facebook_scraping_page', methods=['POST'])
def facebook_scraping_page():
    if request.method == 'POST':
        linkUrl = request.form['link_facebook']
        limit_post = request.form['limit_post']
        posts = []
        for post in get_posts(linkUrl,pages=int(limit_post), options = {'comments':True,"reactors": True}):
            
            posts.append(post)
            print('###############################################################')
            print(post)
            print('###############################################################')
            post_id = post['post_id']
            text = str(post['text'])
            post_text = str(post['post_text'])
            shared_text =str( post['shared_text'])
            original_text = post['original_text']
            time = post['time']
            timestamp = post['timestamp']
            image = str(post['image'])
            image_lowquality = str(post['image_lowquality'])
            images = str(post['images'])
            images_description = str(post['images_description'])
            images_lowquality = str(post['images_lowquality'])
            images_lowquality_description = str(post['images_lowquality_description'])
            video = str(post['video'])
            video_duration_seconds = post['video_duration_seconds']
            video_height = post['video_height']
            video_id = post['video_id']
            video_quality = post['video_quality']
            video_size_MB = post['video_size_MB']
            video_thumbnail = str(post['video_thumbnail'])
            video_watches = post['video_watches']
            video_width = post['video_width']
            likes = post['likes']
            comments = post['comments']
            shares = post['shares']
            post_url = str(post['post_url'])
            link = str(post['link'])
            links = str(post['links'])
            user_id = post['user_id']
            username = str(post['username'])
            user_url = str(post['user_url'])
            is_live = str(post['is_live'])
            factcheck = post['factcheck']
            shared_post_id = post['shared_post_id']
            shared_time = post['shared_time']
            shared_user_id = post['shared_user_id']
            shared_username = str(post['shared_username'])
            shared_post_url = str(post['shared_post_url'])
            available = str(post['available'])
            comments_full = str(post['comments_full'])
            reactors = post['reactors']
            w3_fb_url = post['w3_fb_url']
            reactions = post['reactions']
            reaction_count = post['reaction_count']
            with_ = str(post['with'])
            page_id = post['page_id']
            sharers = post['sharers']
            image_id = post['image_id']
            image_ids = str(post['image_ids'])
            # was_live = str(post['was_live'])
            # header = str(post['header'])
            
            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO `fb_emp3` (`post_id`, `text`, `post_text`, `shared_text`, `original_text`, `time`, `timestamp`, `image`, `image_lowquality`, `images`, `images_description`, `images_lowquality`, `images_lowquality_description`, `video`, `video_duration_seconds`, `video_height`, `video_id`, `video_quality`, `video_size_MB`, `video_thumbnail`, `video_watches`, `video_width`, `likes`, `comments`, `shares`, `post_url`, `link`, `links`, `user_id`, `username`, `user_url`, `is_live`, `factcheck`, `shared_post_id`, `shared_time`, `shared_user_id`, `shared_username`, `shared_post_url`, `available`, `comments_full`, `reactors`, `w3_fb_url`, `reactions`, `reaction_count`, `with`, `page_id`, `sharers`, `image_id`, `image_ids`, `was_live`, `header`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(post_id,text,post_text,shared_text,original_text,time,timestamp,image,image_lowquality,images,images_description,images_lowquality,images_lowquality_description,video,video_duration_seconds,video_height,video_id,video_quality,video_size_MB,video_thumbnail,video_watches,video_width,likes,comments,shares,post_url,link,links,user_id,username,user_url,is_live,factcheck,shared_post_id,shared_time,shared_user_id,shared_username,shared_post_url,available,comments_full,reactors,w3_fb_url,reactions,reaction_count,with_,page_id,sharers,image_id,image_ids,'was_live','header'))
            mysql.connection.commit()
        print(linkUrl)
    return 'Los datos se cargaron a la base de datos correctamente, porfavor vuelve al inicio'

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# INSERT INTO fb_emp3 VALUES(2252600314895487)