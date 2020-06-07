from conversation.conversation import get_response
from persistence.logs import log_response, log_request, log_error
from integration.util import is_message_old

################################################
# this class is here to keep simple, telegram
# could be replaced by another messenger later
# then the imports below should be changed
################################################

from integration.tgram import connect as tgram_connect
from integration.tgram import parse_message, send_message

def process_json(js):
    try:
        message = parse_message(js)
        log_request(message=message)
        response = get_response(message)
        send_reply_message(message=message, response=response, reply=is_message_old(message))
    except Exception:
        log_error()
        raise

def send_reply_message(message, response, reply=False):
    try:
        log_response(message=message, response=response)
        send_message(last_message=message, response=response, reply=reply)
    except Exception:
        log_error()
        raise

def connect():
    try:
        tgram_connect()
    except Exception:
        log_error()
        raise
