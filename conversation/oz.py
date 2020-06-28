from persistence.settings import is_oz_enabled, disable_oz, enable_oz
from persistence.logs import get_message, get_last_request


def is_oz_on(message):
    # cache it for 5 minutes or something
    is_on = message["chat_id"] not in ["222772"] and is_oz_enabled()
    print("oz is on: ", is_on)
    return is_on


def respond_oz_message(message):
    # cannot import earlier because of circular dependency
    from integration.integration import send_reply_message
    text = message["text"]
    if text == "oz on":
        enable_oz()
        send_reply_message(message, "oz on", {"move": "oz on"})
        return None, {"move": "oz on"}
    if text == "oz off":
        disable_oz()
        send_reply_message(message, "oz off", {"move": "oz off"})
        return None, {"move": "oz off"}
    parts = text.split()
    if len(parts) >= 5 and parts[0] == "oz" and parts[3] == "text":
        print("using oz text to respond")
        chat_id = parts[1]
        msg_id = parts[2]
        old_message = get_message(chat_id, msg_id)
        last = get_last_request(chat_id)
        is_old = last["msg_id"] != msg_id
        send_reply_message(old_message, " ".join(parts[4:]), {"move": "oz text"}, is_old)
        return "sent", {"move": "oz text"}
    raise RuntimeError("bad message from oz")


def is_oz_message(message):
    is_oz = message["chat_id"] == "798772222" and message["text"].startswith("oz")
    print("got message from oz: ", is_oz)
    return is_oz


def log_to_oz(message):
    # cannot import earlier because of circular dependency
    print("asking oz to reply")
    from integration.integration import send_reply_message
    send_reply_message(_create_forward_message_for_oz(message),
                       "{} {} {}".format(message["chat_id"], message["msg_id"], message["text"]), {"move": "oz ask"})
    return None, {"move": "oz ask"}


def _create_forward_message_for_oz(message):
    return {"chat_id": "798772222",
            "text": message["text"],
            "language": message["language"],
            "date": message["date"],
            "msg_id": message["msg_id"]}
