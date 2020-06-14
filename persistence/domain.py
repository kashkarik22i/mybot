from datetime import datetime, timedelta
from datetime import timezone

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
    return get_moods_in_range(message, datetime.utcnow() - timedelta(days=7))


def get_moods_in_range(message, from_date, to_date=None):
    if not to_date:
        to_date = datetime.utcnow()
        to_date = to_date.replace(tzinfo=timezone.utc)
    chat_id = message["chat_id"]
    db = firestore.Client()
    collection = db.collection('moods')
    docs = collection.where('chat_id', '==', chat_id)\
        .where('date', ">=", from_date)\
        .where('date', "<=", to_date).stream()
    return [doc.to_dict() for doc in docs]


def delete_all_chat_moods(message):
    db = firestore.Client()
    docs = db.collection('moods').where('chat_id', '==', message["chat_id"]).stream()
    for doc in docs:
        doc.reference.delete()


if __name__ == "__main__":
    time = datetime.utcnow()
    print(get_moods_in_range({"chat_id": "798772222"}, time - timedelta(minutes = 120)))
