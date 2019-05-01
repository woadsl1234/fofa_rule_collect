from flask import Flask, render_template
app = Flask(__name__)
import utils.database as DB
import random

def get_color(value):
    color = ['error', 'success','info' ,'warning']
    return random.choice(color)

app.add_template_filter(get_color,'get_color')

@app.route('/')
@app.route('/index')
def index():
    db = DB.DBTool('./fofa.db')
    T = db.executeQuery('select * from data order by ID desc')
    res = T.fetchall()

    return render_template("index.html", data = res)

if __name__ == '__main__':
    app.run()