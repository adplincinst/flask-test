# MUST BE FIRST: Monkey patch the standard library to make 
# blocking calls (like time.sleep) non-blocking.
from gevent import monkey
from time import sleep
monkey.patch_all()

import time
import click
from flask import Flask, Blueprint, jsonify, request, make_response
from gevent.pywsgi import WSGIServer

# 1. Setup
APP = Flask(__name__)
BLUEPRINT = Blueprint('gevent_api', __name__)

# 2. Execution Wrapper
def execute_from_flask(api_function, *args):
    content, status = api_function(*args)
    return make_response(jsonify(content), status)

# 3. Core Logic
def get_status_data():
    """
    Even though we use standard time.sleep, gevent's 
    monkey-patching makes this non-blocking!
    """
    time.sleep(10) 
    return {
        "status": "online",
        "mode": "Gevent (Greenlets)",
        "message": "I slept for 10s using standard time.sleep()!"
    }, 200

# 4. Route Definition
@BLUEPRINT.route('/status')
def status_endpoint():
    sleep(10)
    return execute_from_flask(get_status_data)

APP.register_blueprint(BLUEPRINT)

# 5. CLI Entry Point
@click.command()
@click.option('--port', default=5000, help='Port to run on')
def serve(port):
    address = ('0.0.0.0', port)
    # We use Gevent's WSGI server instead of the Flask dev server
    http_server = WSGIServer(address, APP)
    
    click.echo(f"Gevent server running on http://0.0.0.0:{port}")
    http_server.serve_forever()

if __name__ == '__main__':
    serve()

