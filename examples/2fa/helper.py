from cpaassdk import Client
from constants import (
  CLIENT_ID,
  CLIENT_SECRET,
  BASE_URL,
  DESTINATION_NUMBER,
  DESTINATION_EMAIL
)

def initialise_client():
  client = Client({
      'client_id': CLIENT_ID,
      'client_secret': CLIENT_SECRET,
      'base_url': BASE_URL
  })
  return client

def send_twofactor_code(email):
  client = initialise_client()
  if email:
    params = {
      'message': 'Your verification code {code}',
      'destination_address': DESTINATION_EMAIL,
      'method': 'email',
      'subject': 'Twofactor verification'
    }
    response = client.twofactor.send_code(params)
    return response
  else:
    params = {
      'message': 'Your verification code {code}',
      'destination_address': DESTINATION_NUMBER,
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
