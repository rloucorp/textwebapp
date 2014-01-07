from filters import val_ago, human_date
from flask import render_template, Flask
import datetime as dt

app = Flask(__name__)

#Instead of using database define json for template to render
def get_excerpts():
    data = [
        {"content": "It was the best of times, it was the worst of times, it was the age of widsom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair.", "author": "Charles Dickens", "title": "A Tale of Two Cities","year": 1859},
        {"content": "Call me Ishmael.", "author": "Herman Melville", "title": "Moby Dick", "year": 1851}
    ]
    return data
    
def get_content():
    data = [
        {"content": "This is a test post #1!!", "score": 150, "address": "1"},
        {"content": "And test post 2 is here!", "score": 50, "address": "2"},
        {"content": "And test post 3 is here!", "score": 10, "address": "1.1"}
    ]
    return data


#Functions calls using python decorators
@app.route('/')
def index():
    excerptdata = get_excerpts()
    contentdata = get_content()
    return render_template("index.html", rows=contentdata,excerpts=excerptdata)

@app.template_filter()
def seconds_ago(val):
    return val_ago(val, unit="second")

@app.route('/experiment')
def experiment():
    return render_template('seconds.jinja2.html',
                           seconds=range(60))

app.add_template_filter(human_date)

@app.route('/datetest')
def datetest():
    now = dt.datetime.now()
    deltas = [
        dt.timedelta(seconds=5),
        dt.timedelta(seconds=60*60),
        dt.timedelta(days=5),
        dt.timedelta(days=60)
    ]
    dates = [(now - delta)
                for delta in deltas]
    return render_template('dates.jinja2.html',
                            dates=dates)

if __name__ == "__main__":
    app.run(debug=True)
