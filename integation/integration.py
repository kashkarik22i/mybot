from conversation.conversation import get_response
from persistence.logs import log_response, log_request, log_error
from integation.util import is_message_old

################################################
# this class is here to keep simple, telegram
# could be replaced by another messenger later
# then the imports below should be changed
################################################

from integation.tgram import connect as tgram_connect
from integation.tgram import parse_message, send_message

def process_json(js):
    try:
        message = parse_message(js)
        log_request(message=message)

        response = get_response(message)
        log_response(message=message, response=response)

        # TODO move to a messaging system later
        # small hack to be able to return messages as replies if bot was dead
        # logic could go to mastermind
        if is_message_old(message):
            send_message(last_message=message, response=response, reply=True)
        else:
            send_message(last_message=message, response=response)
    except Exception:
        log_error()
        raise 

def connect():
    tgram_connect()
