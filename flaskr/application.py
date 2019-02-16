from flask import Flask, request, url_for, render_template
from twitter_utils import user_exists
from map_creation import build_map
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/handle_user', methods=['POST'])
def handle_user():
    user_name = request.form['username']
    limit = request.form['limit']
    if str.isdigit(limit):
        limit = int(limit)
    else:
        limit = None
    if not user_exists(user_name):
        return render_template('index.html',error='invalid_user_name')
    else:
        result = build_map(user_name, limit)
        if result != None:
            return render_template(user_name+'map.html')
        else:
            return render_template('index.html',error='no_friends')


if __name__ == '__main__':
    app.run()