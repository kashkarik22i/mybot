from conversation.dialog.dialogmanager import DialogManager
from conversation.nlg.generator import NLG
from conversation.nlu.analyzer import NLU
from integation.actions import act_on_move

def get_response(msg) -> str:

    msg_parsed = NLU().parse(msg)
    move = DialogManager().get_next_move(msg_parsed)
    act_on_move(msg, move)

    return NLG().make_answer(move)
