import os
import io
from aylienapiclient import textapi

def summarize(text):
    print("inside python script")

    client = textapi.Client("001761ba", "dd668154d01ac3ec48250a068538aa9a")

    #url = 'https://www.microsoft.com/en-us/Useterms/Retail/Windows/10/UseTerms_Retail_Windows_10_English.htm'
    title = ''

    #EDIT HERE
    #f = open(os.getcwd() + '/text1.txt', 'r')

    # f = open(text_path, 'r')
    #text = f.read()

    #summary = client.Summarize({'url': url, 'title': title, 'text' = text, 'sentences_number': 3, 'sentences_percentage': 40})
    summary = client.Summarize({'title':title,'text': text, 'sentences_percentage': 30})
    #summary = client.Summarize({'url':url, 'sentences_percentage': 50})

    #f.close()
    #f2 = open('/home/raunaks/paralegal/summarizing/summary.txt','w')

    f2 = open('/summary.txt','w')

    for sentence in summary['sentences']:
        f2.write('\n' + sentence)
        #print(sentence)
    f2.close()
