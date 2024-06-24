from flask import Flask,jsonify,request


app = Flask(__name__)

todos = [ { "label": "My first task", "done": False }]
@app.route('/todos',methods=['GET'])
def hello_world():
    print(todos)
    json_todos = jsonify(todos)
    return json_todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    json_todos = jsonify(todos)
    return json_todos

@app.route('/todos/<int:position>',methods=['DELETE'])
def delete_todo(position):
    print('this is the position to delete',position)
    del todos[position]
    json_todos = jsonify(todos)
    return json_todos

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)