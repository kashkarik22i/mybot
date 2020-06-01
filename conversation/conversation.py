from conversation.actions import act_on_move
from conversation.dialog.dialogmanager import DialogManager
from conversation.nlg.generator import NLG
from conversation.nlu.analyzer import NLU
from conversation.nlu.languages import detect_language


def get_response(msg) -> str:

    print("got text message :", msg["text"])
    language = detect_language(msg)
    msg_parsed = NLU().parse(msg, language)
    move = DialogManager().get_next_move(msg_parsed)
    print("detected move {move}".format(move=move["move"]))
    act_on_move(msg, move)

    return NLG().make_answer(move, language)
