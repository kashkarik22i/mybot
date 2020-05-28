def detect_intent_texts(text, language_code):
    project_id = 'massive-rock-278120' 
    #project_id = 'newagent-ykcdro'
    import uuid
    session_id = str(uuid.uuid4())
    import dialogflow_v2 as dialogflow
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    #print('Session path: {}\n'.format(session))

    text_input = dialogflow.types.TextInput(
        text=text, language_code=language_code)

    query_input = dialogflow.types.QueryInput(text=text_input)
 
    response = session_client.detect_intent(
        session=session, query_input=query_input)

    #print('=' * 20)
    #print('Query text: {}'.format(response.query_result.query_text))
    #print('Detected intent: {} (confidence: {})\n'.format(
    #    response.query_result.intent.display_name,
    #    response.query_result.intent_detection_confidence))
    #print('Fulfillment text: {}\n'.format(
    #    response.query_result.fulfillment_text))
    return response.query_result.intent.display_name, response.query_result.intent_detection_confidence

if __name__ == "__main__":
  detect_intent_texts("hi", "en_US")
