from google.cloud import firestore

def save_chat_language(message, language):
    # wrong place to put it but speed is more important than cleaneliness
    if language == "german":
        language = "de"
    if language == "russian":
        language = "ru"
    db = firestore.Client()
    doc_ref = db.collection('chats').document(str(message["chat_"]))
    doc_ref.set({
      'text': message["text"],
      'date': str(message["date"]),
      'language': language
    })
