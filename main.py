import os
from wsgiref import simple_server
from flask import Flask, session, request, Response, jsonify

app = Flask(__name__)

@app.route('/', methods = ['GET' , 'POST'])
def index():
    return 'Flask app is running'

if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5001
    httpd = simple_server.make_server(host = host , port = port , app = app)
    httpd.serve_forever()