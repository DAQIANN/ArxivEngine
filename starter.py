from flask import Flask, request, render_template
from datetime import datetime
from searchStart import whooshFinder
from splittingtexts import get_sents
import json
import spacy

app = Flask(__name__)

#Setup: export FLASK_APP=starter.py
#Run: flask run
# this one can just do python3 starter.py

def start():
    global find 
    find = whooshFinder("small_combine.txt")

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        lines = find.whooshFind(form_data["Index"])
        lines.remove('')
        return render_template('data.html',form = lines )
    if request.method == 'return':
        form()
 
 
if __name__ == "__main__":
    # Launch the Flask dev server
    print("Please wait while the data is being prepared...")
    start()
    app.run(host="localhost", debug=True, use_reloader=False)
