from flask import Flask, render_template, request, json
import os
import io
import sys
from aylienapiclient import textapi

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/summarize', methods = ['POST'])
def summarize():
    text = request.form['form_input']
    print(text)

    client = textapi.Client("001761ba", "dd668154d01ac3ec48250a068538aa9a")

    title = ''
    summary = client.Summarize({'title':title,'text': text, 'sentences_percentage': 30})

    f2 = open(os.getcwd()+'/summary.txt','w')

    total_summary = ""
    for sentence in summary['sentences']:
        # print(sentence)
        f2.write('\n' + sentence)
        total_summary = total_summary + "\n" + sentence
    f2.close()

    # print(total_summary)
    return render_template('index.html', summary=total_summary)
    # return total_summary

@app.route('/query', methods = ['POST'])
def query():
    import subprocess
    text = request.form['form_input']
    query = request.form['query']
    jsonString = "{\"passage\":\"" + text + "\", \"question\":\"" + query + "\"}"
    print(jsonString)
    file = open(os.getcwd() + "/tmp.jsonl", "w+")
    file.write(str(jsonString));
    file.close()

    subprocess.call(["python3.6", "-m", "allennlp.run", "predict", "bidaf-model-2017.09.15-charpad.tar.gz", os.getcwd() + "/tmp.jsonl"])

    return render_template('index.html')

if __name__ == '__main__':
  app.run()
