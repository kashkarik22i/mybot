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
    chat_id = update.message.chat.id
    msg_id = update.message.message_id
    date = update.message.date
    text = update.message.text.encode('utf-8').decode()
    language = update.message.from_user.language_code
    print("language: ", language)
    print("got text message :", text)
    # todo use proper object
    return {"chat_id": chat_id,
            "msg_id": msg_id,
            "date": date,
            "text": text,
            "language": language}

def send_message(last_message, response, reply=False):
    chat_id = last_message["chat_id"]
    if reply:
        bot.sendMessage(chat_id=chat_id, text=response, reply_to_message_id=last_message["msg_id"])
    else:
        bot.sendMessage(chat_id=chat_id, text=response)
