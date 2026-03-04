from flask import Flask, Blueprint, jsonify, request, make_response
from time import sleep

# 1. Define the Blueprint
BLUEPRINT = Blueprint('api_v1', __name__)

# 2. Pygeoapi-style execution wrapper
def execute_from_flask(api_function, *args):
    """Bridge between Flask and core logic."""
    content, status = api_function(*args)
    response = make_response(jsonify(content), status)
    return response

# 3. Core Logic
def get_status_data():
    return {
        "status": "online",
        "server": "Gunicorn/WSGI",
        "concurrency": "Multi-threaded"
    }, 200

# 4. Route defined on the Blueprint
@BLUEPRINT.route('/status')
def status_endpoint():
    sleep(10)
    return execute_from_flask(get_status_data)

# 5. App Instantiation and Blueprint Registration
def create_app():
    app = Flask(__name__)
    app.register_blueprint(BLUEPRINT)
    return app

APP = create_app()
