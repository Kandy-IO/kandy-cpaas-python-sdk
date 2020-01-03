from flask import Flask, render_template, request, redirect, session
import os
from helper import send_twofactor_code, verify_code
from constants import (
  TEST_EMAIL,
  TEST_PASSWORD,
  DESTINATION_EMAIL,
  DESTINATION_NUMBER
)

app = Flask(__name__)

@app.route('/')
def base():
  return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if session.get('logged_in'):
    return redirect('/dashboard')
  alert = None
  if request.method == 'POST':
    if request.form['email'] != TEST_EMAIL or request.form['password'] != TEST_PASSWORD:
      alert = 'Invalid Credentials. Please try again.'
      return render_template('login.html', alert=alert)
    else:
      session['cred_verified'] = True
      return redirect('/verify')
  return render_template('login.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
  if session.get('logged_in'):
    return redirect('/dashboard')
  if not session.get('cred_verified'):
    return redirect('/login')
    
  alert = None
  if request.method == 'POST':
    code_id = session.get('code_id')
    response = verify_code(code_id, request.form['code'])
    if response['verified']:
      session['logged_in'] =  True
      return redirect('/dashboard')
    else:
      alert = response['message']
      return render_template('verify.html', alert=alert)
  return render_template('verify.html')

@app.route('/sendtwofactor', methods=['POST'])
def sendtwofactor():
  otp = request.form['otp']
  if (otp == 'email') and not DESTINATION_EMAIL:
    alert = 'please enter a destination email in your constants file.'
    return render_template('verify.html', alert=alert)
  if (otp == 'sms') and not DESTINATION_NUMBER:
    alert = 'please enter a destination number in your constants file.'
    return render_template('verify.html', alert=alert)
  email = True if (otp == 'email') else False
  res = send_twofactor_code(email)
  session['code_id'] = res['code_id']
  success_msg = 'Twofactor authentication code sent succesfully.'
  return render_template('verify.html', success_msg=success_msg)  

@app.route('/dashboard', methods=['GET'])
def dashboard():
  if not session.get('logged_in'):
    return redirect('/login')
  else:
    return render_template('dashboard.html')

@app.route('/logout', methods=['GET'])
def logout():
  session['logged_in'] = False
  return redirect('/')

if __name__=='__main__':
  app.secret_key = os.urandom(12)
  app.run()