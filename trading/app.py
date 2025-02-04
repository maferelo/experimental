from flask import Flask, request, jsonify
from redis import Redis
from rq import Queue
from worker import background_task

app = Flask(__name__)
redis_conn = Redis(host='redis', port=6379)
task_queue = Queue(connection=redis_conn)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/task', methods=['POST'])
def add_task():
    task = task_queue.enqueue(background_task, request.json.get('name'))
    return jsonify({'task_id': task.id}), 202