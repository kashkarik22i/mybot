from conversation.nlg.generator import NLG
from conversation.nlu.analyzer import NLU
from conversation.dialog.dialogmanager import DialogManager

def get_response(msg) -> str:
    text = msg["text"] # there is more in here

    msg_parsed = NLU().parse(text)
    move = DialogManager().get_next_move(msg_parsed)

    return NLG().make_answer(move)
