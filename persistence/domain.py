from datetime import datetime, timedelta
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

def get_moods_for_week(message):
    return get_moods_in_range(message, datetime.now() - timedelta(days = 7))

def get_moods_in_range(message, from_date, to_date=None):
    if not to_date:
        to_date = datetime.now()
    chat_id = message["chat_id"]
    db = firestore.Client()
    collection = db.collection('moods')
    docs = collection.where('chat_id', '==', chat_id)\
        .where('date', ">=", from_date)\
        .where('date', "<=", to_date).stream()
    return [doc.to_dict() for doc in docs]


if __name__ == "__main__":
    print(get_moods_in_range({"chat_id": "798772222"}, datetime.now() - timedelta(hours = 30)))
