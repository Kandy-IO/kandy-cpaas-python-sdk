from flask import Flask, render_template, request, redirect, session
import os, json
from helper import send_sms, subscribe, notification_parse

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def base():
  alert = None
  if request.method == 'POST':
    msg_response = send_sms(request.form['message'], request.form['number'])
    if 'exception_id' in msg_response:
      message = msg_response['message']
      return render_template('index.html', alert=True, message=message)
    elif 'delivery_info' in msg_response:
      message = 'Message sent successfully.'
      return render_template('index.html', success=True, message=message)
  else:
    if not session.get('notifications'):
      if os.path.isfile('notification.txt'):
        os.remove('notification.txt')
    else:
      session['notifications'] = 'active-session'
  return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe_notification():
  if request.method == 'POST':
    webhook_url = request.form['webhook'] + '/webhook'
    response = subscribe(webhook_url)
    if 'subscription_id' in response:
      session['notifications'] = []
      message = 'Created subscription'
      return render_template('index.html', success=True, message=message)
    else:
      alert = True
      message = response['message']
      return render_template('index.html', alert=True, message=message)

@app.route('/webhook', methods=['POST'])
def notification_webhook():
  response = notification_parse(request.get_json())
  with open('notification.txt', 'a') as f:
    f.write("%s\n" % response)
  return ('', 204)

@app.route('/notifications', methods=['GET', 'POST'])
def notifications():
  if os.path.isfile('notification.txt'):
    with open('notification.txt') as f:
      notification_list = f.readlines()
    notification_list = [x.strip() for x in notification_list] 
    return json.dumps(notification_list)
  return '[]'

if __name__=='__main__':
  app.secret_key = os.urandom(12)
  app.run(debug=True)
