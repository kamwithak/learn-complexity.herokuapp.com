from flask import Flask, render_template, request
import os, random, copy
from werkzeug.useragents import UserAgent

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'photos')

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

def shuffle(q):
  """
  This function is for shuffling 
  the dictionary elements.
  """
  global selected_questions
  global questions
  selected_questions = {}

  curNumberOfQuestions, questionMax = 0, 6
  while(curNumberOfQuestions < questionMax):
    current_selection = random.choice(list(q.keys()))
    if current_selection not in selected_questions:
      selected_questions[current_selection] = q[current_selection]
      curNumberOfQuestions += 1
  
  questions = copy.deepcopy(selected_questions)

  return selected_questions

@app.route('/')
def quiz():
  agent = UserAgent(request.headers.get('User-Agent'))

  if (agent.platform in ['blackberry', 'android', 'iphone', 'ipad']):
    message = f'<h1>Please access LearnComplexity.io from a computer 🖥️<br> Your {agent.platform} device is not supported! ⏰</h1>'
    return message

  selected_questions = shuffle(original_questions)
  for key in questions: random.shuffle(questions[key])
  print(questions)
  return render_template('main.html', q=selected_questions, o=questions)

@app.route('/quiz', methods=['POST'])
def quiz_answers():
  correct = 0
  for key in selected_questions:
    answered = request.form[key]
    # print(f'Selected Answer: {answered} - Correct Answer: {selected_questions[key][0]} ')
    if selected_questions[key][0] == answered:
      correct += 1
    # print(correct)
  return '<h1>Correct Answers: <u>'+str(correct)+'</u></h1>'

if __name__ == '__main__':
  app.run(debug=True)