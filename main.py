from flask import Flask, render_template, request, json, url_for, redirect
import os
import io
import sys
from aylienapiclient import textapi
from werkzeug import secure_filename
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine

UPLOAD_FOLDER = os.getcwd()+'/uploads'
ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
  return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/summarize_text', methods = ['POST'])
def summarize_text():
    text = request.form['form_input']
    return render_template('index.html', summary=compute_summary(text))

@app.route('/summarize_pdf', methods=['POST', 'GET'])
def summary_pdf():
    file = request.files['inputFile']
    filename = secure_filename(file.filename)
    file.save(str(os.getcwd()) + "/uploads/" + filename)
    fp = open(str(os.getcwd())+"/uploads/"+filename, 'rb')
    doc = PDFDocument()
    parser = PDFParser(fp)
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize('')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    laparams.char_margin = 1.0
    laparams.word_margin = 1.0
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    extracted_text = ''
    for page in doc.get_pages():
        interpreter.process_page(page)
        layout = device.get_result()
        for lt_obj in layout:
            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                extracted_text += lt_obj.get_text()

    return render_template('index.html', summary=compute_summary(extracted_text))

def compute_summary(text):
    client = textapi.Client("001761ba", "dd668154d01ac3ec48250a068538aa9a")
    title = ''
    summary = client.Summarize({'title':title,'text': text, 'sentences_percentage': 35})
    total_summary = ""
    for sentence in summary['sentences']:
        import re
        section_sign_code = u'\u00A7'

        regex = r"^(( )*(\()?( )*([0-9]+|[a-z]|[A-Z])( )*(\)|\.))"
        matches = re.finditer(regex, sentence)
        offset = 0
        for matchNum, match in enumerate(matches):
            print(match.group())
            offset = match.end()

        sentence = sentence[offset:].strip().capitalize()
        print(sentence, file=sys.stdout)
        total_summary = total_summary + "<br/>" + sentence[offset:].strip().capitalize()


    return total_summary

@app.route('/submit_rating', methods=['POST', 'GET'])
def rating():
    stars = request.form['stars']
    return redirect('/')

if __name__ == '__main__':
  app.run()
