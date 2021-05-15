from flask import Flask, render_template, request
from summarize import summarize
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def input_form():
    return render_template('input.html')

@app.route('/', methods = ['POST'])
def call_summarize():
    # name of the tag you want to get
    text = request.form['text']
    sentence_count = int(request.form['number'])
    language = request.form['language']
    # print(text)
    # print(sentence_count)
    # print(language)
    summary = summarize(text,sentence_count,language)
    # print(summary)
    # return render_template('output.html')
    return render_template('output.html',result=summary,text=text,sentence_count=sentence_count)

if __name__ == '__main__':
    app.run(debug=True)