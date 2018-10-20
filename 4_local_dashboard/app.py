import os
import operator

from flask import Flask, render_template, url_for, json

app = Flask(__name__)

@app.route('/')
def index():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

    stats_url = os.path.join(SITE_ROOT, "static/data", "stats.json")
    stats = json.load(open(stats_url))

    categories_url = os.path.join(SITE_ROOT, "static/data", "category.json")
    categories = json.load(open(categories_url))
    sorted_categories = sorted(categories.items(), key=operator.itemgetter(1), reverse=True)

    authors_url = os.path.join(SITE_ROOT, "static/data", "author.json")
    authors = json.load(open(authors_url))
    sorted_authors = sorted(authors.items(), key=operator.itemgetter(1), reverse=True)

    weekdays_url = os.path.join(SITE_ROOT, "static/data", "weekday.json")
    weekdays = json.load(open(weekdays_url))

    return render_template('index.html', stats=stats, categories=sorted_categories, authors=sorted_authors, weekdays=weekdays)

if __name__ == '__main__':
    app.run(debug=True)
