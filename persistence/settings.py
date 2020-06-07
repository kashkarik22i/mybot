from google.cloud import firestore

def save_chat_language(message, language):
    db = firestore.Client()
    doc_ref = db.collection('chats').document(str(message["chat_id"]))
    doc_ref.set({
      'text': message["text"],
      'date': message["date"],
      'language': language
    })

def get_chat_language(message):
    db = firestore.Client()
    doc = db.collection('chats').document(str(message["chat_id"])).get()
    if doc.exists:
        return doc.to_dict()["language"]
    else:
        return None

def enable_oz():
    db = firestore.Client()
    doc_ref = db.collection('oz_settings').document("settings")
    doc_ref.set({
      'enabled': True
    })

def disable_oz():
    db = firestore.Client()
    doc_ref = db.collection('oz_settings').document("settings")
    doc_ref.set({
      'enabled': False
    })

def is_oz_enabled():
    db = firestore.Client()
    doc = db.collection('oz_settings').document("settings").get()
    if doc.exists:
        return doc.to_dict()["enabled"]
    else:
        return False
