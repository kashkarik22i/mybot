from conversation.actions import act_on_move
from conversation.dialog.dialogmanager import DialogManager
from conversation.languages import detect_language
from conversation.nlg.generator import NLG
from conversation.nlu.analyzer import NLU
from conversation.oz import is_oz_on, respond_oz_message, log_to_oz, is_oz_message
from persistence.logs import get_last


def get_response(message):
    print("got text message :", message["text"])
    message = _prepare_message(message)
    if is_oz_message(message):
        respond_oz_message(message)
        return
    msg_parsed = NLU().parse(message, message["language"])
    move = DialogManager().get_next_move(msg_parsed)
    print("detected move {move}".format(move=move["move"]))
    action = act_on_move(message, move)
    if move["move"] == "next" and is_oz_on(message):
        log_to_oz(message)
        return None
    return NLG().make_answer(move, message["language"], action), move


def _prepare_message(message):
    message["text"] = message["text"].casefold()  # everything is case insensitive for now in dialog part
    language = detect_language(message)
    message["language"] = language
    last = get_last(message["chat_id"])
    if last is not None:
        message["last_move"] = last
    return message
