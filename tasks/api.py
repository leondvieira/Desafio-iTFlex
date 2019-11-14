from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [

]


@app.route('/api/tasks')
def list():

    return jsonify(tasks), 200


@app.route('/api/tasks', methods=['POST'])
def create_task():
    task = request.get_json()
    task['id'] = len(tasks)
    tasks.append(task)
    return jsonify(task), 201


@app.route('/api/tasks/<int:id>', methods=['PUT'])
def done_task(id):

    for task in tasks:
        if task['id'] == id:
            done = request.get_json('done')
            task['done'] = done['done']
            return jsonify(task), 200

    return jsonify({'error': 'not found'}), 404


@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):

    for task in tasks:
        if task['id'] == id:
            del tasks[id]
            return jsonify(tasks), 204

    return jsonify({'error': 'not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)