from google.cloud import firestore
from google.cloud import storage
from conversation.secrets import BUCKET_NAME
from datetime import datetime
import uuid
import traceback
from datetime import datetime


def log_request(message):
    db = firestore.Client()
    doc_ref = db.collection('requests').document(str(uuid.uuid4()))
    doc_ref.set({
      'msg_id': message["msg_id"],
      'text': message["text"],
      'chat_id': message["chat_id"],
      'date': message["date"],
      'language': message["language"]
    })


def log_response(message, response, analysis):
    db = firestore.Client()
    doc_ref = db.collection('responses').document(str(uuid.uuid4()))
    doc_ref.set({
      'msg_id': message["msg_id"],
      'text': message["text"],
      'chat_id': message["chat_id"],
      'date': message["date"],
      'response': response,
      'move': analysis["move"],
      'language': message["language"],
      'last_move': message.get("last_move")
    })


def are_there_past_responses(message):
    return get_last_response(message['chat_id']) is not None


def get_message(chat_id, msg_id):
    db = firestore.Client()
    collection = db.collection('requests')
    docs = collection.where('chat_id', '==', chat_id)\
        .where('msg_id', "==", msg_id).stream()
    return [doc.to_dict() for doc in docs][0]


def get_last_response(chat_id):
    db = firestore.Client()
    collection = db.collection('responses')
    docs = collection.where('chat_id', '==', chat_id)\
        .order_by("date", direction=firestore.Query.DESCENDING).limit(1).stream()
    as_dicts = [doc.to_dict() for doc in docs]
    if len(as_dicts) > 0:
        return as_dicts[0]
    else:
        return None


def get_last_request(chat_id):
    db = firestore.Client()
    collection = db.collection('requests')
    docs = collection.where('chat_id', '==', chat_id)\
        .order_by("date", direction=firestore.Query.DESCENDING).limit(1).stream()
    as_dicts = [doc.to_dict() for doc in docs]
    if len(as_dicts) > 0:
        return as_dicts[0]
    else:
        return None


def log_error():
    db = firestore.Client()
    doc_ref = db.collection('errors').document(str(uuid.uuid4()))
    error_message = traceback.format_exc()
    doc_ref.set({
      'text': str(error_message),
      'date': datetime.utcnow()
    })


def _get_all_as_files():
    run = str(datetime.utcnow())
    db = firestore.Client()
    collection = db.collection('responses')
    docs = [doc.to_dict() for doc in collection.stream()]
    chats = set(doc["chat_id"] for doc in docs)
    for chat_id in chats:
        filename = 'responses_{}.txt'.format(chat_id)
        with open(filename, "w") as f:
            _write_chat(run, docs, chat_id, f, filename)


def _write_chat(run, docs, chat_id, f, filename):
    these_docs = [doc for doc in docs if doc["chat_id"] == chat_id]
    these_docs = sorted(these_docs, key=lambda doc: doc["date"])
    for doc in these_docs:
        f.write('USER: {}\nBOT: {}\t(MOVE: {})\n'.format(doc["text"], doc["response"], doc.get("move")))
    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(run + "/" + chat_id)
    blob.upload_from_filename(filename)


if __name__ == "__main__":
    print(get_last("798772222"))
