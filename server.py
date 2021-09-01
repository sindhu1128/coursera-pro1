import translator,tests
from flask import Flask, render_template, request
import json


app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    tr_text=translator.get_eng_to_french(textToTranslate)
    return tr_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    tr_text=translator.get_fr_to_english(textToTranslate)
    return tr_text

@app.route("/")
def renderIndexPage():
    return render_template('index.html')
    

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=8080)
    app.run(debug=True)

