from datetime import datetime
 
from flask import Flask, render_template
from flask import request
import json

import win32ui

app = Flask(__name__)
 
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
 
@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html', posts=posts)
 
@app.route('/about')
def about():
    o = win32ui.CreateFileDialog( 1, ".txt", "default.txt", 0, "Text Files (*.txt)|*.txt|All Files (*.*)|*.*|")
    o.DoModal()
    print (o.GetPathName())
    
    return render_template('about.html', title='About')

@app.route('/api', methods=['POST']) 
def api():
    d = request.get_json()
    to = d['to']

    d = {"text": "Hello {}".format(to)}
    return json.dumps(d)
    
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=False)




#https://opentutorials.org/module/3669/22003
#https://wikidocs.net/143921
#https://wikidocs.net/book/4542