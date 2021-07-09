from flask.json import jsonify
from flask import Flask, render_template, request
from step05jasun import lee
from myself import js, scrape


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/', methods=["GET"])
def basic():


    if request.method =="GET":
        return render_template('index.html')
    

@app.route('/box', methods=["GET"])
def box():
    x = scrape()
    # print(x)
    return jsonify(x)

@app.route('/pan', methods=["GET", "POST"])
def pan():
    y = js()
   
    # print(y)
    return jsonify(y)

@app.route('/plot', methods=['POST'])
def plot():

  return '{"img01" : "./static/images/chart01.png"}'


if __name__=="__main__":
    app.run(debug = True, host="127.0.0.1", port="5000")