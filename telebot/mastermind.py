def get_response(msg: str, chat_id: str) -> str:
    """
    you can place your mastermind AI here
    could be a very basic simple response like "معلش"
    or a complex LSTM network that generates appropriate answer
    """

    msg_parsed = NLU().parse(msg)
    move = DialogManager().get_next_move(msg_parsed)

    return NLG().make_answer(move)
