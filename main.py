from flask import Flask, render_template, request, json
import os
import io
import sys
from aylienapiclient import textapi

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/handle_data', methods = ['POST'])
def handle_data():
    text = request.form['form_input']
    print("FORM HAS BEEN PROCESSED")

    client = textapi.Client("001761ba", "dd668154d01ac3ec48250a068538aa9a")

    title = ''
    summary = client.Summarize({'title':title,'text': text, 'sentences_percentage': 30})

    f2 = open(os.getcwd()+'/summary.txt','w')

    for sentence in summary['sentences']:
        f2.write('\n' + sentence)
    f2.close()

    return render_template('index.html')

if __name__ == '__main__':
  app.run()
