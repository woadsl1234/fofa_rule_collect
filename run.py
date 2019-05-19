from flask import Flask, render_template, abort, jsonify
app = Flask(__name__)
import utils.database as DB
import random

def get_color(value):
    color = ['error', 'success','info' ,'warning']
    return random.choice(color)

app.add_template_filter(get_color,'get_color')

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    db = DB.DBTool('./fofa.db')
    T = db.executeQuery('select * from data order by ID desc')
    res = T.fetchall()
    pagenum = len(res)//10+1

    return render_template("index.html", data = res, pagenum = xrange(pagenum))

@app.route('/page/<int:id>', methods=['GET'])
def page(id):
    db = DB.DBTool('./fofa.db')
    T = db.executeQuery('select * from data order by ID desc '+'limit '+ str((id-1)*10)+',10')
    res = T.fetchall()
    T = db.executeQuery('select * from data order by ID desc')
    pagenum = len(T.fetchall())//10+1

    return render_template("index.html", data = res , pagenum = xrange(pagenum))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
