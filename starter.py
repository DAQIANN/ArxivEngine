from flask import Flask, request, render_template
from datetime import datetime
from searchStart import whooshFinder
from splittingtexts import get_subject, get_sents
import json
import spacy

app = Flask(__name__)

#Setup: export FLASK_APP=starter.py
#Run: flask run
# this one can just do python3 starter.py

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        lines = get_sents("combine.txt")
        print(form_data["Index"])
        subj = get_subject(lines, form_data["Index"])
        print(subj[0])
        return render_template('data.html',form = subj )
    if request.method == 'return':
        form()
 
 
#app.run(host='localhost', port=5000)


if __name__ == "__main__":
     # Launch the Flask dev server
     app.run(host="localhost", debug=True)
