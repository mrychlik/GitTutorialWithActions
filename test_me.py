# This file will be located by pytest and functions will be executed
import datetime

def test_datetime():
    print(datetime.datetime.now().strftime('%Y:%m:%d:%H:%M:%S'))


def test_word_count():
    file = open("README.md", "rt")
    data = file.read()
    words = data.split()
    print('Number of words in text file :', len(words))
