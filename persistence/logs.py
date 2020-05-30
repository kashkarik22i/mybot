from google.cloud import firestore

def log_request(message):
    db = firestore.Client()
    doc_ref = db.collection('requests').document(str(message["msg_id"]))
    doc_ref.set({
      'text': message["text"],
      'chat_id': message["chat_id"],
      'date': str(message["date"]),
    })

def log_response(message, response):
    db = firestore.Client()
    doc_ref = db.collection('responses').document(str(message["msg_id"]))
    doc_ref.set({
      'text': message["text"],
      'chat_id': message["chat_id"],
      'date': str(message["date"]),
      'response': response
    })
