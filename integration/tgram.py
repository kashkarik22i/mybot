import telegram
from conversation.secrets import TOKEN, URL

###############################################
# this class is here to keep telegram specifics
# it may be relatively hard to test thus needs
# to be slim and tested manually
###############################################

global bot
bot = telegram.Bot(token=TOKEN)


def connect():
    return bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))


def parse_message(js):
    update = telegram.Update.de_json(js, bot)
    # TODO, add update.update_id and use it to identify repeated broken messages
    chat_id = update.message.chat.id
    msg_id = update.message.message_id
    date = update.message.date
    text = update.message.text.encode('utf-8').decode()
    language = update.message.from_user.language_code
    # todo use proper object
    return {"chat_id": str(chat_id),
            "msg_id": str(msg_id),
            "date": date,
            "text": text,
            "language": language}


def send_message(last_message, response, reply=False):
    chat_id = last_message["chat_id"]
    if response is not None:
        if reply:
            bot.sendMessage(chat_id=chat_id, text=response, reply_to_message_id=last_message["msg_id"])
        else:
            bot.sendMessage(chat_id=chat_id, text=response)
