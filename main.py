from flask import Flask, render_template, redirect, send_from_directory, url_for, request
import os, random, copy
from werkzeug.useragents import UserAgent
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
import requests
from oauthlib.oauth2 import WebApplicationClient
# from db import init_db_command
from user import User
import json
import logging
# import sqlite3

app = Flask(__name__)
app.secret_key = 'x4thHzLCyrLUpznsy1wKXSXW'
client_id = '360742249219-992pv8f1bsh7or9h9b5tpg3g7q62ve60'

# gunicorn_logger = logging.getLogger('gunicorn.error')
# app.logger.handlers = gunicorn_logger.handlers
# app.logger.setLevel(gunicorn_logger.level)

app.config['UPLOAD_FOLDER'] = os.path.join('static', 'photos')

login_manager = LoginManager()
login_manager.init_app(app)


# Naive database setup
# try:
#   init_db_command()
# except sqlite3.OperationalError:
#   # Assume it's already been created
#   pass

client = WebApplicationClient(client_id=client_id)

original_questions = {
  os.path.join(app.config['UPLOAD_FOLDER'], 'a.PNG') : ['O(N)','O(N^2)','O(Log(N))','O(1)'],
  os.path.join(app.config['UPLOAD_FOLDER'], 'b.PNG') : ['O(N)','O(Log(N))','O(N*Log(N))','O(1)'],
  os.path.join(app.config['UPLOAD_FOLDER'], 'c.PNG') : ['O(N)','O(N^2)','O(Log(N))','O(N*Log(N))'],
  os.path.join(app.config['UPLOAD_FOLDER'], 'd.PNG') : ['O(N^2)','O(N)','O(Log(N))','O(1)'],
  os.path.join(app.config['UPLOAD_FOLDER'], 'e.PNG') : ['O(N)','O(N^2)','O(Log(N))','O(1)'],
  os.path.join(app.config['UPLOAD_FOLDER'], 'f.PNG') : ['O(2^N)','O(N^2)','O(Log(N))','O(N!)'],
  os.path.join(app.config['UPLOAD_FOLDER'], 'g.PNG') : ['O(N)','O(N^3)','O(Log(N))','O(N^2)'],
  os.path.join(app.config['UPLOAD_FOLDER'], 'h.PNG') : ['O(Log(N))','O(1)','O(N^2)','O(N)'],
  os.path.join(app.config['UPLOAD_FOLDER'], 'i.PNG') : ['O(Log(N))','O(N^3)','O(1)','O(N)'],
  os.path.join(app.config['UPLOAD_FOLDER'], 'j.PNG') : ['O(N)','O(N^2)','O(Log(N))','O(N!)'],
  os.path.join(app.config['UPLOAD_FOLDER'], 'k.PNG') : ['O(N)','O(N^2)','O(Log(N))','O(1)'],
  os.path.join(app.config['UPLOAD_FOLDER'], 'l.PNG') : ['O(Log(N))','O(N^3)','O(N*Log(N))','O(N)'],
  os.path.join(app.config['UPLOAD_FOLDER'], 'g.PNG') : ['O(N)','O(N^3)','O(N*Log(N))','O(Log(N))']
}

selected_questions = {}
questions = {}
question_max = 6

def get_google_provider_cfg():
  return requests.get("https://accounts.google.com/.well-known/openid-configuration").json()

def shuffle(q):
  """
  This function is for shuffling 
  the dictionary elements.
  """
  global selected_questions
  global questions
  selected_questions = {}
  curNumberOfQuestions = 0
  
  while(curNumberOfQuestions < question_max):
    current_selection = random.choice(list(q.keys()))
    if current_selection not in selected_questions:
      selected_questions[current_selection] = q[current_selection]
      curNumberOfQuestions += 1
  
  questions = copy.deepcopy(selected_questions)

  return selected_questions

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/favicon.ico')
def favicon():
  return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def main():
  if (current_user.is_authenticated):
    name = current_user.name
    # email = current_user.email
    # profile_pic = current_user.profile_pic
    app.logger.debug(name)
    return f"<h1>Authenticated - {current_user.name}</h1><br><a href='/logout'>Sign Out</a>"
  else:
    return redirect(location='/welcome')

@app.route('/welcome')
def welcome():
  agent = UserAgent(request.headers.get('User-Agent'))
  if (agent.platform in ['blackberry', 'android', 'iphone', 'ipad']):
    message = f'<h1>Your {agent.platform} device is currently unsupported⏰<br> Please access LearnComplexity.io from a computer 🖥️</h1>'
    return message

  return render_template('welcome.html')

@app.route('/fundamentals')
def fundamentals():
  agent = UserAgent(request.headers.get('User-Agent'))

  if (agent.platform in ['blackberry', 'android', 'iphone', 'ipad']):
    message = f'<h1>Your {agent.platform} device is currently unsupported⏰<br> Please access LearnComplexity.io from a computer 🖥️</h1>'
    return message
  return render_template('fundamentals.html')

@app.route('/time-complexity')
def time():
  agent = UserAgent(request.headers.get('User-Agent'))

  if (agent.platform in ['blackberry', 'android', 'iphone', 'ipad']):
    message = f'<h1>Your {agent.platform} device is currently unsupported⏰<br> Please access LearnComplexity.io from a computer 🖥️</h1>'
    return message
  return render_template('time-complexity.html')

@app.route('/space-complexity')
def space():
  agent = UserAgent(request.headers.get('User-Agent'))

  if (agent.platform in ['blackberry', 'android', 'iphone', 'ipad']):
    message = f'<h1>Your {agent.platform} device is currently unsupported⏰<br> Please access LearnComplexity.io from a computer 🖥️</h1>'
    return message
  return render_template('space-complexity.html')

@app.route('/earn')
def earn():
  return redirect(location='https://youtu.be/dQw4w9WgXcQ?t=42')

@app.route('/problems')
def problems():
  agent = UserAgent(request.headers.get('User-Agent'))

  if (agent.platform in ['blackberry', 'android', 'iphone', 'ipad']):
    message = f'<h1>Your {agent.platform} device is currently unsupported⏰<br> Please access LearnComplexity.io from a computer 🖥️</h1>'
    return message

  selected_questions = shuffle(original_questions)
  for key in questions: random.shuffle(questions[key])
  # print(questions)
  return render_template('problems.html', q=selected_questions, o=questions)

@app.route('/result', methods=['POST'])
def quiz_answers():
  if (len(request.form)==question_max):
    correct = 0
    for key in selected_questions:
      answered = request.form[key]
      # print(f'Selected Answer: {answered} - Correct Answer: {selected_questions[key][0]} ')
      if selected_questions[key][0] == answered:
        correct += 1
      # print(correct)
    if (correct == question_max):
      return render_template('success.html')
    else:
      return render_template('failure.html')
  else:
    return redirect("/problems")

@app.route('/login')
def login():
  google_provider_cfg = get_google_provider_cfg()
  authorization_endpoint = google_provider_cfg["authorization_endpoint"]

  request_uri = client.prepare_request_uri(
      authorization_endpoint,
      redirect_uri=request.base_url + "/callback",
      scope=["openid", "email", "profile"],
  )

  return redirect(request_uri)

@app.route("/login/callback")
def callback():
  code = request.args.get("code")
  google_provider_cfg = get_google_provider_cfg()
  token_endpoint = google_provider_cfg["token_endpoint"]
  token_url, headers, body = client.prepare_token_request(
      token_endpoint,
      authorization_response=request.url,
      redirect_url=request.base_url,
      code=code
  )
  token_response = requests.post(
      token_url,
      headers=headers,
      data=body,
      auth=(client_id, app.secret_key)
  )
  client.parse_request_body_response(json.dumps(token_response.json()))
  userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
  uri, headers, body = client.add_token(userinfo_endpoint)
  userinfo_response = requests.get(uri, headers=headers, data=body)
  if userinfo_response.json().get("email_verified"):
    unique_id = userinfo_response.json()["sub"]
    users_email = userinfo_response.json()["email"]
    picture = userinfo_response.json()["picture"]
    users_name = userinfo_response.json()["given_name"]
  else:
    return "User email not available or not verified by Google.", 400
  
  user = User(
    id_=unique_id, name=users_name, email=users_email, profile_pic=picture
  )

  if not User.get(unique_id):
    User.create(unique_id, users_name, users_email, picture)

  login_user(user)

  return redirect(url_for("main"))

@app.route("/logout")
@login_required
def logout():
  logout_user()
  return redirect(url_for("main"))

if __name__ == '__main__':
  app.run()