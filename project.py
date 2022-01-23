from flask import Flask, jsonify, request
app = Flask(__name__)

data = [
    {
        'id' : 1,
        'Name' : 'Vaishnavi',
        'Contact' : '7877282728', 
        'done' : False
    },
    {
        'id' : 2,
        'Name' : 'Akshaya',
        'Contact' : '8292828198', 
        'done' : False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message" : "Please provide the data!"
        }, 400)

    contact = {
        'id' : data [-1] ['id'] + 1,
        'Name' : request.json['Name'],
        'Contact' : request.json.get('Contact', ""),
        'done' : False
    }
    data.append(contact)
    return jsonify({
        "status" : "success",
        "message" : "Contact added succesfully!"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : data
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)