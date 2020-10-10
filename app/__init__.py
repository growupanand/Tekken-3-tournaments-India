from flask import Flask, render_template, url_for
import json
import os

with open('data.json') as f:
  data = json.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/view_match/<match_name>')
def view_match(match_name):
    match = []
    for item in data:
        if item['match_name'] == match_name:
            match = item
            images = []
            if os.path.isdir('app/static/images/' + match_name):
                for image in os.listdir('app/static/images/' + match_name):
                    images.append(url_for('static', filename='images/' + match_name + '/' + image))
            match['images'] = images

    return render_template('view_match.html', match=match)



if __name__ == "__main__":
    app.run()