from conversation.nlg.generator import NLG
from conversation.nlu.analyzer import NLU
from conversation.dialog.dialogmanager import DialogManager

def get_response(msg) -> str:

    msg_parsed = NLU().parse(msg)
    move = DialogManager().get_next_move(msg_parsed)

    return NLG().make_answer(move)
