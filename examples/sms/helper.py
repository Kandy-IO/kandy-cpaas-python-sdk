from kandycpaas import Client
from constants import (
  CLIENT_ID,
  CLIENT_SECRET,
  BASE_URL,
  DESTINATION_NUMBER,
  SENDER_NUMBER
)

def initialise_client():
  client = Client({
      'client_id': CLIENT_ID,
      'client_secret': CLIENT_SECRET,
      'base_url': BASE_URL
  })
  return client

def send_sms(message, destination_number=DESTINATION_NUMBER):
  client = initialise_client()
  params = {
    'type': 'sms',
    'message': message,
    'destination_address': destination_number,
    'sender_address': SENDER_NUMBER
  }
  try:
    response = client.conversation.create_message(params)
    return response
  except Exception as error:
    return error

def subscribe(webhook_url):
  client = initialise_client()
  params = {
    'type': 'sms',
    'webhook_url': webhook_url,
    'destination_address': SENDER_NUMBER
  }
  response = client.conversation.subscribe(params)
  return response

def notification_parse(notification):
  client = initialise_client()
  notification_resp = client.notification.parse(notification)
  return notification_resp
  