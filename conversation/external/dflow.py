import dialogflow_v2 as dialogflow
import uuid
from conversation.secrets import PROJECT_ID

def detect_intent_texts(text, language_code):
    print("language for dialogflow {}".format(language_code))
    session_id = str(uuid.uuid4())
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(
        text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(
        session=session, query_input=query_input)
    #print('Fulfillment text: {}\n'.format(
    #    response.query_result.fulfillment_text))
    return response.query_result.intent.display_name, response.query_result.intent_detection_confidence

if __name__ == "__main__":
  detect_intent_texts("hi", "en_US")
