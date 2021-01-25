
from os import remove
from flask import Flask, render_template, request
from coronabot import chatbot
from preprocessors import remove_stopwords_question, stemming_corpus, stemming_query

app = Flask(__name__)
app.static_folder = 'static'


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    userText = remove_stopwords_question(userText)
    userText = stemming_query(userText)
    print(userText)
    return str(chatbot.get_response(userText.lower()))


if __name__ == "__main__":
    app.run()
