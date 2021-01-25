# for data crawl
import pandas as pd
import requests
import numpy as np
from bs4 import BeautifulSoup
import os
import time
from preprocessors import stemming_corpus, remove_stopwords_corpus

# for chatbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# ***************************************** data crawl start*****************************
# sending request to grab html
URL = "https://www.worldometers.info/coronavirus/country/malaysia/"
html_page = requests.get(URL).text

# Beutifulsoup extracting table data
soup = BeautifulSoup(html_page, 'lxml')

# Find date
finddate = soup.find('div', class_="news_date")
date = finddate.text

# find new case
soup("div", id=("news_block"))
soup.findAll('div', id=("news_block"))
kes = soup.find('li', class_="news_li")
kesbaru = kes.find('strong')

# data cleaning
unprocesskes = kesbaru.text
processkes = (unprocesskes[:unprocesskes.find('new cases')])

# combine date and new cases
# combine
x = "kes baharu pada "+date+" ialah "+processkes+" kes."


# training file

a = 'apakah kes baru'
b = 'kes baharu'
c = 'kes hari ini'
d = 'new case'
e = 'kes paling baru'
g = 'kes baru'

# save as text
f = open("kesbaru.txt", "w")
f.write(str(a))
f.write('\n')
f.write(x)
f.write('\n')
f.write(b)
f.write('\n')
f.write(x)
f.write('\n')
f.write(c)
f.write('\n')
f.write(x)
f.write('\n')
f.write(d)
f.write('\n')
f.write(x)
f.write('\n')
f.write(e)
f.write('\n')
f.write(x)
f.write('\n')
f.write(g)
f.write('\n')
f.write(x)
f.write('\n')
f.close()


# ***************************************** data crawl end*****************************

# ****************************************chatbot start*************************************
# Creating ChatBot Instance
chatbot = ChatBot(
    'INFOCOVID CHATBOT',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        # 'chatterbot.logic.MathematicalEvaluation',  # math function
        # 'chatterbot.logic.TimeLogicAdapter', #time function
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Saya minta maaf, tetapi saya tidak faham apa yang anda tulis. saya masih belajar.',
            'maximum_similarity_threshold': 0.90
        },
        # 'chatterbot.logic.BestMatch',
    ],
    database_uri='sqlite:///database.sqlite3',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
)

# Training with Personal Ques & Ans


# preprocessing the training file
remove_stopwords_corpus("training_data/covid3.txt")  # output: filteredtext
stemming_corpus("training_data/filteredtext.txt")  # output: stemmedtext

training_data_greeting = open(
    'training_data/greeting malay3.txt').read().splitlines()
training_data_covid = open(
    'training_data/stemmedtext.txt').read().splitlines()
training_data_kesbaru = open('kesbaru.txt').read().splitlines()
# it to update to new date

training_data = training_data_greeting + \
    training_data_covid + training_data_kesbaru

trainer = ListTrainer(chatbot)
trainer.train(
    training_data,
)
# ****************************************chatbot end*************************************
