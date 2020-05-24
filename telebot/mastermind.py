from telebot.nlg.generator import NLG
from telebot.nlu.analyzer import NLU
from telebot.dialog.dialogmanager import DialogManager

def get_response(msg: str) -> str:
    """
    you can place your mastermind AI here
    could be a very basic simple response like "معلش"
    or a complex LSTM network that generates appropriate answer
    """

    msg_parsed = NLU().parse(msg)
    move = DialogManager().get_next_move(msg_parsed)

    return NLG().make_answer(move)
