from datetime import datetime
 
from flask import Flask, render_template
from flask import request
import json
import threading
import youtube_dl
from youtube_dl.utils import args_to_str

#import win32ui


app = Flask(__name__)

numcount=0
posts = [
    {
        'author': {
            'username': 'test-user'
        },
        'title': '첫 번째 포스트',
        'content': '첫 번째 포스트 내용입니다.',
        'date_posted': datetime.strptime('2018-08-01', '%Y-%m-%d')
    },
    {
        'author': {
            'username': 'test-user'
        },
        'title': '두 번째 포스트',
        'content': '두 번째 포스트 내용입니다.',
        'date_posted': datetime.strptime('2018-08-03', '%Y-%m-%d')
    },
]

finish_log=""
class MyLogger(object):
    def debug(self, msg):
        print(msg)

    def warning(self, msg):
        print(msg)

    def error(self, msg):
        print(msg)

def my_hook(d):
    global finish_log
    try:
        finish_log=d['_percent_str']+d['_eta_str']
    except AttributeError:
        print('AttributeError')
    if d['status'] == 'finished':
        finish_log="Done downloading, now converting ..."

def download_yt(url):
	ydl_opts = {
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	 ydl.download([url])
     
     


@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html', posts=posts)
 
@app.route('/about')
def about():
    return render_template('about.html', title='About')

    
"""def s():
    o = win32ui.CreateFileDialog( 1, ".jpg", "default.jpg", 0, "jpg Files (*.jpg)|*.jpg|All Files (*.*)|*.*|")
    o.DoModal()
    print (o.GetPathName())
"""
@app.route('/api', methods=['POST']) 
def api():
    d = request.get_json()
    to = d['to']

    d = {"text": "Hello {}".format(to)}
    return json.dumps(d)
@app.route('/youtube',methods=['POST','GET'])
def youtube():
    global finish_log
    if request.method == 'POST':
        finish_log=""
        value = request.form['test']
        """ydl =threading.Thread(target=download_yt(value))
        ydl.start()"""
        a=threading.Thread(target=download_yt,args=(value,)) 
        a.start()
        return render_template('youtube.html',test=finish_log,title='Youtube')
    elif request.method=='GET':
        return render_template('youtube.html',test=finish_log,title='Youtube')



if __name__ == "__main__":
    app.debug=True
    app.run(host='0.0.0.0', port=8080, debug=False)




#https://opentutorials.org/module/3669/22003
#https://wikidocs.net/143921
#https://wikidocs.net/book/4542
#https://essim92.tistory.com/8
#https://airfox1.tistory.com/2?category=1118519 
#https://woolbro.tistory.com/91
