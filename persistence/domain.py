from google.cloud import firestore
import uuid

def save_mood(message, mood):
    db = firestore.Client()
    doc_ref = db.collection('moods').document(str(uuid.uuid4()))
    doc_ref.set({
      'text': message["text"],
      'mood': mood,
      'msg_id': str(message["msg_id"]),
      'chat_id': message["chat_id"],
      'date': message["date"]
    })
