from flask import Flask, render_template, request, redirect, session
import os
from helper import send_twofactor_code, verify_code
from constants import (
  TEST_EMAIL,
  TEST_PASSWORD
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
      res = send_twofactor_code()
      session['code_id'] = res['code_id']
      return redirect('/verify')
  return render_template('login.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
  if session.get('logged_in'):
    return redirect('/dashboard')
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