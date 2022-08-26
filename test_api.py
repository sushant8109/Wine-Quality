from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return {"Hello":"Sushant Analyst"}

@app.route("/sum",methods=['POST'])
def get_sum():
    a = request.form['a']
    b = request.form['b']
    out = int(a) + int(b)
    return jsonify(out)

@app.route("/product",methods=['POST'])
def get_product():
    a = request.form['a']
    b = request.form['b']
    out = int(a) * int(b)
    return jsonify(out)

if __name__=='__main__':
    app.run(debug=True)
