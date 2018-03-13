from flask import Flask, render_template

app = Flask(__name__)

#@app.route('/')
#def hello_world():
#  return 'Bansuri Makhanchorwale'

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/handle_data', methods = ['POST'])
def handle_data():
 	text = request.form['form_input']
 	print(text)

#@app.route('/getconfig', methods=['GET', 'POST'])
#def config():
#    value = request.form['config']
#    print ("This is the user value :  ", value);

if __name__ == '__main__':
  app.run()
