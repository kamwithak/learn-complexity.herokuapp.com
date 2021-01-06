from flask import Flask, render_template, request
import os, random, copy

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'photos')

original_questions = {
  os.path.join(app.config['UPLOAD_FOLDER'], 'a.PNG') : ['O(N)','O(N^2)','O(Log(N))','O(1)'],
  os.path.join(app.config['UPLOAD_FOLDER'], 'b.PNG') : ['O(N)','O(Log(N))','O(N*Log(N))','O(1)'],
  os.path.join(app.config['UPLOAD_FOLDER'], 'c.PNG') : ['O(N)','O(N^2)','O(Log(N))','O(N*Log(N))'],
  os.path.join(app.config['UPLOAD_FOLDER'], 'd.PNG') : ['O(N^2)','O(N)','O(Log(N))','O(1)']
}

questions = copy.deepcopy(original_questions)

def shuffle(q):
  """
  This function is for shuffling 
  the dictionary elements.
  """
  selected_keys = []
  i = 0
  while i < len(q):
    current_selection = random.choice(list(q.keys()))
    if current_selection not in selected_keys:
      selected_keys.append(current_selection)
      i = i+1
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
  for i in questions.keys():
    answered = request.form[i]
    if original_questions[i][0] == answered:
      correct = correct+1
  return '<h1>Correct Answers: <u>'+str(correct)+'</u></h1>'

if __name__ == '__main__':
  app.run(debug=True)