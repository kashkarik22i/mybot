from flask import Flask, request
import traceback
from conversation.secrets import TOKEN
from integration.integration import process_json, connect

app = Flask(__name__)

@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    try:
        process_json(request.get_json(force=True))
    except Exception:
        # TODO this is not amazing, but avoids repeated messages
        # answering later IMO does not make sense for this bot yet
        error_message = traceback.format_exc()
        print(error_message)
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
