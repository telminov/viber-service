SEND_TEXT = 'send_text'
SEND_IMAGE = 'send_image'
SEND_TEXT_AND_BUTTON = 'send_text_and_button'

CHECK_STATUS_MESSAGES = 'check_status_messages'

API = [SEND_TEXT, SEND_IMAGE, SEND_TEXT_AND_BUTTON, CHECK_STATUS_MESSAGES]
API_CHOICES = [(api, api) for api in API]