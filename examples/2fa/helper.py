from kandycpaas import Client
from constants import (
  CLIENT_ID,
  CLIENT_SECRET,
  BASE_URL,
  SENDER_NUMBER
)

def initialise_client():
  client = Client({
      'client_id': CLIENT_ID,
      'client_secret': CLIENT_SECRET,
      'base_url': BASE_URL
  })
  return client

def send_twofactor_code():
  client = initialise_client()
  params = {
    'message': 'Your verification code {code}',
    'destination_address': DESTINATION_NUMBER,
    'sender_address': SENDER_NUMBER
  }
  response = client.twofactor.send_code(params)
  return response


def verify_code(code_id, verification_code):
  client = initialise_client()
  params = {
    'code_id': code_id,
    'verification_code': verification_code
  }
  response = client.twofactor.verify_code(params)
  return response
  