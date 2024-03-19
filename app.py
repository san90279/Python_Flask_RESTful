from flask import Flask,jsonify, request
import json
from Models.Result import ResultList, Result


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

result_list = ResultList()
isInit=True

# /tasks(GET)
@app.route('/tasks', methods=['GET'])
def get_tasks():
    global isInit
    if(len(result_list.result)==0 and isInit):
        result_list.add_result(1, "task", 0)
        isInit=0
    return jsonify(result_list.to_json())

# /task(POST)
@app.route('/task', methods=['POST'])
def create_task():
    request_data = request.json
    if 'text' in request_data:
        text = request_data['text']
        id=len(result_list.result)+1
        result_list.add_result(id, text, 0)
        task=None
        for result_item in result_list.result:
            if result_item.id == id:
                task = result_item
                break
        return jsonify(task.to_json()), 201    

# /task(PUT)
@app.route('/task/<int:id>', methods=['PUT'])
def update_task(id):
    request_data = request.json
    if 'text' in request_data and 'status' in request_data and id:
        task=None
        for result_item in result_list.result:
            if result_item.id == id:
                task = result_item
                break
        if task is None:
            return jsonify({'error': 'Result not found'}), 404
        task.text = request_data['text']
        return jsonify(task.to_json())

# /task(DELETE)
@app.route('/task/<int:id>', methods=['DELETE'])
def delete_task(id):
    task=None
    for result_item in result_list.result:
        if result_item.id == id:
            task = result_item
            break
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    
    result_list.result.remove(task)
    return '', 200



if __name__ == '__main__':
    app.run(debug=True)