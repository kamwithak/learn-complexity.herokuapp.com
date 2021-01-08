from flask import Flask, render_template, request
import os, random, copy

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
  os.path.join(app.config['UPLOAD_FOLDER'], 'g.PNG') : ['O(Log(N))','O(N^3)','O(N*Log(N))','O(N)']
}

selected_keys = []
curNumberOfQuestions = 0
questions = copy.deepcopy(original_questions)

def shuffle(q):
  """
  This function is for shuffling 
  the dictionary elements.
  """
  global curNumberOfQuestions
  global selected_keys
  selected_keys = []
  curNumberOfQuestions, questionMax = 0, 6
  while(curNumberOfQuestions < questionMax):
    current_selection = random.choice(list(q.keys()))
    if current_selection not in selected_keys:
      selected_keys.append(current_selection)
      curNumberOfQuestions += 1
  return selected_keys

@app.route('/')
def quiz():
  questions_shuffled = shuffle(questions)
  for i in questions.keys():
    random.shuffle(questions[i])
  return render_template('main.html', q=questions_shuffled, o=questions)

@app.route('/quiz', methods=['POST'])
def quiz_answers():
  correct = 0
  for i in range(len(selected_keys)):
    answered = request.form[selected_keys[i]]
    if original_questions[selected_keys[i]][0] == answered:
      correct += 1
  return '<h1>Correct Answers: <u>'+str(correct)+'</u></h1>'

if __name__ == '__main__':
  app.run(debug=True)