from flask import Flask, jsonify, request;

app = Flask(__name__);

@app.route("/", methods=['GET'])

def hello():
    return jsonify({"Greeting" : "Hello Everybody!!!"});

@app.route("/", methods=['POST'])

def abc():
    return jsonify({"Finish" : "Good Bye!!!"});

@app.route("/abc/", methods=['GET', 'POST'])

def xyz():
    if request.method=='GET':
        return jsonify({"Welcome" : "GUEST!!!"});
    if request.method=='POST':
        return jsonify({"Bye" : "See you again!!!"});

@app.route("/cube/<int:num>", methods=['GET '])

def cube(num):
    return jsonify({"Cube" : num**3});


if __name__=='__main__':
    app.run(debug = True)
