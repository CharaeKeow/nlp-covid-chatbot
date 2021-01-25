# Remove stopwords ✅
# Stemmalization ✅

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re


'''Stem words in the filtered text (after removing stopwords). This
   should improve the performance of the model as it can now detect
   words such as "adakah" and "ada" as a same words (this explaination
   sucks ^_^).
   The input is the path of the corpus file.
'''


def stemming_corpus(corpus):
    p = re.compile('\?$')  # match ? at the end of line => indicate question
    covid_corpus = open(corpus)  # load covid q&a file

    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    line = covid_corpus.read().splitlines()

    # open file in w mode to overwrite first
    appendFile = open('./training_data/stemmedtext.txt', 'w')
    for words in line:
        m = p.search(words)
        appendFile = open('./training_data/stemmedtext.txt', 'a')
        if m:
            output = stemmer.stem(words)  # stem words and put in output
            for word in output:  # write words into a file
                appendFile.write(""+word)
        else:
            appendFile.write(""+words)
        appendFile.write("\n")
        appendFile.close()


# stemming the user's input query. Return a string

def stemming_query(query):
    factory = StemmerFactory()  # declare the stemmer
    stemmer = factory.create_stemmer()
    output = stemmer.stem(query)  # stem the query

    return output


# stemming_corpus("training_data/covid3.txt")

''' Accept the path of the corpus (eg training_data/text.txt) and it will
    remove the stopwords. Indonesian stopwords from nltk is used due to their
    similarities with Bahasa Melayu stopwords.
    Once the stopwords are removed, the filtered corpus is stored in a new
    filteredtext.txt in training_data directory.
    Note: only remove stopwords from questions only'''


def remove_stopwords_corpus(corpus):

    p = re.compile('\?$')  # match ? at the end of line => indicate question

    # use indonesian stopwords they are roughly similar with us
    stop_words = set(stopwords.words('indonesian'))
    covid_corpus = open(corpus)  # load covid q&a file

    line = covid_corpus.read().splitlines()
    appendFile = open('./training_data/filteredtext.txt', 'w')
    for words in line:
        m = p.search(words)
        # if match, remove stopwords (for question only, as answer want to be kept)
        appendFile = open('./training_data/filteredtext.txt', 'a')
        if m:
            words = words.split()
            for word in words:
                if not word in stop_words:
                    appendFile.write(" "+word)
        else:
            appendFile.write(" "+words)
        appendFile.write("\n")
        appendFile.close()


# removing stopwords from user's query. Retrn a string


def remove_stopwords_question(query):
    stop_words = set(stopwords.words('indonesian'))

    words = word_tokenize(query)
    filtered_sentence = []

    for word in words:
        if not word in stop_words:
            filtered_sentence.append(word)

    return ' '.join(filtered_sentence)  # join string

# remove_stopwords_corpus("training_data/covid3.txt")
