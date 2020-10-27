# This file will be located by pytest and functions will be executed
import date

def test_all():
    file = open("README.md", "rt")
    data = file.read()
    words = data.split()
    print('Number of words in text file :', len(words))
