from flask import Flask, request
from conversation.secrets import TOKEN
from integation.integration import process_json, connect

app = Flask(__name__)

@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    process_json(request.get_json(force=True))
    return 'ok'

@app.route('/connect', methods=['GET', 'POST'])
def connect():
    s = connect()
    if s:
        return "connection setup ok"
    else:
        return "connection setup failed"

if __name__ == '__main__':
    app.run(threaded=True)
