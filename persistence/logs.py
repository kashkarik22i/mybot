from google.cloud import firestore
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

def log_response(message, response):
    db = firestore.Client()
    doc_ref = db.collection('responses').document(str(uuid.uuid4()))
    doc_ref.set({
      'msg_id': message["msg_id"],
      'text': message["text"],
      'chat_id': message["chat_id"],
      'date': message["date"],
      'response': response,
      'language': message["language"]
    })

def get_message(chat_id, msg_id):
    db = firestore.Client()
    collection = db.collection('requests')
    docs = collection.where('chat_id', '==', chat_id)\
        .where('msg_id', "==", msg_id).stream()
    return [doc.to_dict() for doc in docs][0]

def get_last(chat_id):
    db = firestore.Client()
    collection = db.collection('requests')
    docs = collection.where('chat_id', '==', chat_id)\
        .orderBy("date").limit(1).stream()
    return [doc.to_dict() for doc in docs][0]

def log_error():
    db = firestore.Client()
    doc_ref = db.collection('errors').document(str(uuid.uuid4()))
    error_message = traceback.format_exc()
    doc_ref.set({
      'text': str(error_message),
      'date': datetime.utcnow()
    })
