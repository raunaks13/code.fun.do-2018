from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('handle_data', methods = ['POST'])
def handle_data():
    text = request.form['form_input']
    
    print("inside python script")

    client = textapi.Client("001761ba", "dd668154d01ac3ec48250a068538aa9a")

    #url = 'https://www.microsoft.com/en-us/Useterms/Retail/Windows/10/UseTerms_Retail_Windows_10_English.htm'
    title = ''
    #f = open(os.getcwd() + '/text1.txt', 'r')

    # f = open(text_path, 'r')
    #text = f.read()
    summary = client.Summarize({'title':title,'text': text, 'sentences_percentage': 30})

    #f.close()
    #f2 = open('/home/raunaks/paralegal/summarizing/summary.txt','w')

    f2 = open(os.getcwd() + '/summary.txt','w')

    for sentence in summary['sentences']:
        f2.write('\n' + sentence)
        #print(sentence)
    f2.close()


# import subprocess
# process = subprocess.Popen(['python' , 'summarize.py' ], stdout=subprocess.PIPE)
# out, err = process.communicate()
# print(out)

#@app.route('/getconfig', methods=['GET', 'POST'])
#def config():
#    value = request.form['config']
#    print ("This is the user value :  ", value);

if __name__ == '__main__':
  app.run()
