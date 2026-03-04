from flask import Flask, jsonify
import time
import os

app = Flask(__name__)

@app.route('/status')
def get_status():
    # In a standard sync server, this blocks the whole process.
    # In a Gevent worker, this only yields the current greenlet.
    time.sleep(10) 
    
    return jsonify({
        "status": "online",
        "worker_pid": os.getpid(),
        "message": "Slept 10s non-blockingly via Gevent"
    })

if __name__ == "__main__":
    app.run()

