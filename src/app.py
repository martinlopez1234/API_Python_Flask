import flask
from flask import Flask,request
import json



app = Flask(__name__)
todos =  [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
    
]
@app.route('/todos', methods=['GET'])
def hello_world():
   
 

    # puedes convertir esa variable en un string json así
    json_text = flask.jsonify(todos)

    # y luego puedes retornarla (return) en el response body así:
    return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)
    decoded_object = json.loads(request.data)
    todos.append(decoded_object)
    json_textt = flask.jsonify(todos)
    return  json_textt

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    del todos[position]
    json_texttt = flask.jsonify(todos)
    return json_texttt

# Estas dos líneas siempre seben estar al final de tu archivo app.py.

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)