# This file will be located by pytest and functions will be executed
import datetime


def test_arithmetic():
    assert 2+2==4


def test_faulty_arithmetic():
    assert 2+2==5


def test_word_count():
    file = open("README.md", "rt")
    data = file.read()
    words = data.split()
    num_words = len(words)
    assert num_words > 20
