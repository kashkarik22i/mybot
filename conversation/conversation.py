from conversation.actions import act_on_move
from conversation.dialog.dialogmanager import DialogManager
from conversation.languages import detect_language
from conversation.nlg.generator import NLG
from conversation.nlu.analyzer import NLU
from conversation.oz import is_oz_on, respond_oz_message, log_to_oz, is_oz_message


def get_response(message) -> str:
    print("got text message :", message["text"])
    message["text"] = message["text"].casefold() # everything is case insensitive for now in dialog part
    language = detect_language(message)
    if is_oz_message(message):
        respond_oz_message(message)
        return
    msg_parsed = NLU().parse(message, language)
    move = DialogManager().get_next_move(msg_parsed)
    print("detected move {move}".format(move=move["move"]))
    action = act_on_move(message, move)
    if move == "next" and is_oz_on(message):
        log_to_oz(message)
        return None
    return NLG().make_answer(move, language, action)
