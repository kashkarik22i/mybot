from google.cloud import firestore
import uuid
import traceback
from datetime import datetime

def log_request(message):
    db = firestore.Client()
    doc_ref = db.collection('requests').document(str(message["msg_id"]))
    doc_ref.set({
      'text': message["text"],
      'chat_id': message["chat_id"],
      'date': str(message["date"]),
      'language': message["language"]
    })

def log_response(message, response):
    db = firestore.Client()
    doc_ref = db.collection('responses').document(str(message["msg_id"]))
    doc_ref.set({
      'text': message["text"],
      'chat_id': message["chat_id"],
      'date': str(message["date"]),
      'response': response,
      'language': message["language"]
    })

def log_error():
    db = firestore.Client()
    doc_ref = db.collection('responses').document(str(uuid.uuid4()))
    error_message = traceback.format_exc()
    doc_ref.set({
      'text': str(error_message),
      'date': str(datetime.now())
    })
