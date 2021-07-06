from bs4 import BeautifulSoup
from flask.json import jsonify
from flask import Flask, render_template, request
from step05jasun import lee


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/', methods=["GET"])
def basic():


    if request.method =="GET":
        return render_template('index.html')
    

@app.route('/box', methods=["GET"])
def box():
    x = lee()
    # print(x)
    return jsonify(x)



if __name__=="__main__":
    app.run(debug=True)