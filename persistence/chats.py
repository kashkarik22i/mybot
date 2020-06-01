from google.cloud import firestore

def save_chat_language(message, language):
    db = firestore.Client()
    doc_ref = db.collection('chats').document(str(message["chat_id"]))
    doc_ref.set({
      'text': message["text"],
      'date': str(message["date"]),
      'language': language
    })


def get_chat_language(message):
    db = firestore.Client()
    doc = db.collection('chats').document(str(message["chat_id"])).get()
    if doc.exists:
        return doc.to_dict()["language"]
    else:
        return None


if __name__ == "__main__":
    save_chat_language({"chat_id": "798772222", "text": "change lang fake", "date": "2020-05-31 08:20:38"}, "russian")
    print(get_chat_language({"chat_id": "798772222"}))
